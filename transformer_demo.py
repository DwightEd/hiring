"""运行手写 Transformer 前向；随机权重仅用于检查架构与维度。"""
import argparse
import json

import numpy as np

from ai.softmax import softmax
from ai.transformer import Transformer


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=json.loads, default='[[2,5,7,0],[3,6,0,0]]', help='B×S token ID JSON')
    parser.add_argument('--target', type=json.loads, default='[[1,8,9],[1,4,0]]', help='B×T 右移后的目标输入；示例中 1 为 BOS')
    parser.add_argument('--src-vocab-size', type=int, default=32)
    parser.add_argument('--tgt-vocab-size', type=int, default=32)
    parser.add_argument('--d-model', type=int)
    parser.add_argument('--heads', type=int)
    parser.add_argument('--d-ff', type=int)
    parser.add_argument('--layers', dest='num_layers', type=int)
    parser.add_argument('--pad-id', type=int)
    parser.add_argument('--seed', type=int)
    options = parser.parse_args()

    # 未传入的模型参数沿用 Transformer 构造器默认值。
    model_options = {
        name: getattr(options, name)
        for name in ('d_model', 'heads', 'd_ff', 'num_layers', 'pad_id', 'seed')
        if getattr(options, name) is not None
    }
    try:
        source, target = np.asarray(options.source), np.asarray(options.target)
        model = Transformer(options.src_vocab_size, options.tgt_vocab_size, **model_options)
        logits = model.forward(source, target)
    except ValueError as exc:
        parser.error(str(exc))

    probabilities = softmax(logits)
    print(json.dumps({
        'note': '随机权重前向演示；预测不具备语言意义，padding 位置的输出应忽略。',
        'source_shape': list(source.shape),
        'target_shape': list(target.shape),
        'logits_shape': list(logits.shape),
        'predicted_ids': probabilities.argmax(axis=-1).tolist(),
        'probability_sums': probabilities.sum(axis=-1).tolist(),
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
