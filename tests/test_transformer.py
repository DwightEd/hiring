"""Transformer 前向行为测试；无需深度学习框架。"""
import importlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

try:
    import numpy as np
except ImportError:
    np = None


@unittest.skipIf(np is None, 'Transformer 测试需要 NumPy')
class TransformerTests(unittest.TestCase):
    def test_demo_cli(self):
        root = Path(__file__).resolve().parents[1]
        process = subprocess.run(
            [sys.executable, '-X', 'utf8', str(root / 'transformer_demo.py'),
             '--d-model', '12', '--heads', '3', '--layers', '1', '--d-ff', '24',
             '--source', '[[2,3,0]]', '--target', '[[1,4]]'],
            cwd=root, capture_output=True, text=True, encoding='utf-8', check=True,
        )
        result = json.loads(process.stdout)
        self.assertEqual(result['logits_shape'], [1, 2, 32])
        np.testing.assert_allclose(result['probability_sums'], [[1., 1.]])

    def model(self, seed=8):
        module = importlib.import_module('ai.transformer')
        return module.Transformer(12, 13, d_model=8, heads=2, num_layers=2, seed=seed)

    def test_future_target_tokens_cannot_change_prefix(self):
        model = self.model()
        source = np.array([[2, 3, 0], [4, 5, 6]])
        target = np.array([[1, 5, 6, 7], [1, 7, 8, 9]])
        expected = model.forward(source, target)
        changed = target.copy()
        changed[:, 2:] = [[9, 10], [10, 11]]
        actual = model.forward(source, changed)
        np.testing.assert_allclose(actual[:, :2], expected[:, :2], atol=1e-10)
        self.assertFalse(np.allclose(actual[:, 2:], expected[:, 2:]))
        np.testing.assert_allclose(model.forward(source, target[:, :2]), expected[:, :2], atol=1e-10)

    def test_padding_and_batching_preserve_valid_outputs(self):
        model = self.model()
        source = np.array([[2, 3, 0], [4, 0, 0]])
        target = np.array([[1, 5, 6], [1, 7, 0]])
        expected = model.forward(source, target)
        # 分别去掉每个样本的右侧 padding，结果应与批量计算一致。
        np.testing.assert_allclose(model.forward(source[:1, :2], target[:1]), expected[:1], atol=1e-10)
        np.testing.assert_allclose(model.forward(source[1:, :1], target[1:, :2]), expected[1:, :2], atol=1e-10)
        # padding 向量的值不应污染任何有效 token，包括 cross-attention。
        model.src_embedding[0] = 1e4
        model.tgt_embedding[0] = -1e4
        padded_source = np.pad(source, ((0, 0), (0, 2)))
        padded_target = np.pad(target, ((0, 0), (0, 2)))
        actual = model.forward(padded_source, padded_target)[:, :target.shape[1]]
        np.testing.assert_allclose(actual[target != 0], expected[target != 0], atol=1e-10)
        np.testing.assert_array_equal(source, [[2, 3, 0], [4, 0, 0]])
        np.testing.assert_array_equal(target, [[1, 5, 6], [1, 7, 0]])

    def test_target_padding_in_middle_cannot_be_read(self):
        model = self.model()
        source = np.array([[2, 3]])
        target = np.array([[1, 0, 4]])
        expected = model.forward(source, target)
        model.tgt_embedding[0] += 1000
        actual = model.forward(source, target)
        np.testing.assert_allclose(actual[:, [0, 2]], expected[:, [0, 2]], atol=1e-10)

    def test_source_context_and_batch_isolation(self):
        model = self.model()
        source = np.array([[2, 3, 0], [4, 5, 0]])
        target = np.array([[1, 5], [1, 5]])
        expected = model.forward(source, target)
        source[0, 0] = 9
        actual = model.forward(source, target)
        self.assertFalse(np.allclose(actual[0], expected[0]))
        np.testing.assert_allclose(actual[1], expected[1], atol=1e-10)

    def test_all_padding_stays_finite(self):
        with np.errstate(divide='raise', invalid='raise', over='raise'):
            result = self.model().forward(np.zeros((2, 3), dtype=int), np.zeros((2, 2), dtype=int))
        self.assertEqual(result.shape, (2, 2, 13))
        self.assertTrue(np.isfinite(result).all())

    def test_initialization_is_reproducible(self):
        source = np.array([[2, 3]])
        target = np.array([[1, 4, 5]])
        first = self.model(9).forward(source, target)
        np.testing.assert_array_equal(first, self.model(9).forward(source, target))
        self.assertFalse(np.allclose(first, self.model(10).forward(source, target)))

    def test_invalid_dimensions_and_token_ids(self):
        module = importlib.import_module('ai.transformer')
        for options in ({'d_model': 7, 'heads': 2}, {'num_layers': 0}, {'pad_id': -1}, {'d_ff': 0}):
            with self.subTest(options=options), self.assertRaises(ValueError):
                module.Transformer(12, 13, **options)
        model = self.model()
        for source, target in (
            ([[12]], [[1]]), ([[1]], [[13]]), ([[-1]], [[1]]),
            ([[1.5]], [[1]]), ([[1]], [[1.5]]),
            ([[]], [[1]]), ([[1]], [[]]), ([1, 2], [[1]]), ([[1]], [[1], [2]]),
        ):
            with self.subTest(source=source, target=target), self.assertRaises(ValueError):
                model.forward(np.asarray(source), np.asarray(target))

    def test_sinusoidal_positions(self):
        module = importlib.import_module('ai.transformer')
        positions = module.positional_encoding(2, 3)
        expected = [[0., 1., 0.], [np.sin(1.), np.cos(1.), np.sin(10000 ** (-2 / 3))]]
        np.testing.assert_allclose(positions, expected)

    def test_decoder_uses_encoder_memory(self):
        module = importlib.import_module('ai.transformer')
        layer = module.DecoderLayer(4, 2, 6, np.random.default_rng(4))
        layer.self_attention.wo[:] = 0
        layer.cross_attention.wq[:] = 0
        layer.cross_attention.wk[:] = 0
        layer.cross_attention.wv[:] = np.eye(4)
        layer.cross_attention.wo[:] = np.eye(4)
        layer.ffn.w2[:] = 0
        x = np.array([[[1., 0., -1., 0.]]])
        memory = np.array([[[2., 0., 0., -2.], [0., 2., -2., 0.]]])
        expected = x / np.sqrt(.5 + 1e-5)
        expected = expected + [1., 1., -1., -1.]
        expected /= np.sqrt(expected.var(axis=-1, keepdims=True) + 1e-5)
        expected /= np.sqrt(expected.var(axis=-1, keepdims=True) + 1e-5)
        np.testing.assert_allclose(layer.forward(x, memory), expected, atol=1e-10)

    def test_encoder_post_norm_and_residual(self):
        module = importlib.import_module('ai.transformer')
        layer = module.EncoderLayer(4, 2, 6, np.random.default_rng(3))
        layer.self_attention.wq[:] = 0
        layer.self_attention.wk[:] = 0
        layer.self_attention.wv[:] = np.eye(4)
        layer.self_attention.wo[:] = np.eye(4)
        layer.ffn.w2[:] = 0
        layer.ffn.b2[:] = [4., -1., 0., 2.]
        x = np.array([[[1., 0., -1., 0.], [0., 2., 0., -2.]]])

        # 注意力为均匀加权，两个位置都收到 [0.5,1,-0.5,-1]。
        after_residual = x + [.5, 1., -.5, -1.]
        after_norm = after_residual / np.sqrt(after_residual.var(axis=-1, keepdims=True) + 1e-5)
        after_ffn = after_norm + [4., -1., 0., 2.]
        expected = (after_ffn - after_ffn.mean(axis=-1, keepdims=True)) / np.sqrt(
            after_ffn.var(axis=-1, keepdims=True) + 1e-5
        )
        np.testing.assert_allclose(layer.forward(x), expected, atol=1e-10)


if __name__ == '__main__':
    unittest.main()
