"""MHA、MQA、GQA 统一实现
分类：Transformer
题意：x 为 B×T×D，Q 头数 H，KV 头数 G 且 H%G=0；传入各投影矩阵，可选因果遮罩。
思路：投影后显式拆头，G 个 KV 头供各组 Q 头共享，再合并投影。
复杂度：O(BTD²+BT²D) 常规稠密计算；O(BHT²) 注意力空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np
from ai.attention import attention

def multihead_attention(x, wq, wk, wv, wo, heads, kv_heads=None, causal=True):
    b, t, d = x.shape
    kv_heads = heads if kv_heads is None else kv_heads
    if d % heads or heads % kv_heads:
        raise ValueError('D 必须是 H 的整数倍，H 必须是 KV 头数的整数倍')
    width = d // heads
    q = (x @ wq).reshape(b, t, heads, width).transpose(0, 2, 1, 3)
    k = (x @ wk).reshape(b, t, kv_heads, width).transpose(0, 2, 1, 3)
    v = (x @ wv).reshape(b, t, kv_heads, width).transpose(0, 2, 1, 3)
    # 手撕版复制 KV 便于理解；生产内核可用分组广播避免实际复制。
    k, v = np.repeat(k, heads // kv_heads, axis=1), np.repeat(v, heads // kv_heads, axis=1)
    mask = np.tril(np.ones((t, t), dtype=bool)) if causal else None
    output, _ = attention(q, k, v, mask)
    return output.transpose(0, 2, 1, 3).reshape(b, t, d) @ wo
