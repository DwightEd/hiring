"""LoRA 线性层及合并权重
分类：Transformer
题意：x 最后一维 Din；W 为 Din×Dout，A 为 Din×r，B 为 r×Dout。
思路：输出 xW+(alpha/r)(xA)B；合并时 W'=W+(alpha/r)AB。
复杂度：附加 O(Nr(Din+Dout)) 时间，O(r(Din+Dout)) 参数。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def lora_linear(x, weight, a, b, alpha):
    return x @ weight + (alpha / a.shape[1]) * ((x @ a) @ b)

def merge(weight, a, b, alpha):
    return weight + (alpha / a.shape[1]) * (a @ b)
