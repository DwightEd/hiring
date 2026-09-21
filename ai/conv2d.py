"""二维卷积前向
分类：计算机视觉
题意：x 为 NCHW，kernel 为 OIHW；stride/padding 为整数，返回 N×O×Ho×Wo。
思路：实现深度学习中的互相关，不翻转卷积核；循环空间位置，einsum 聚合通道和核。
复杂度：O(N·O·Ho·Wo·I·Kh·Kw)，临时空间为补零输入及输出。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def conv2d(x, kernel, bias=None, stride=1, padding=0):
    x, kernel = np.asarray(x, dtype=float), np.asarray(kernel, dtype=float)
    n, channels, h, w = x.shape
    out_channels, _, kh, kw = kernel.shape
    padded = np.pad(x, ((0,0),(0,0),(padding,padding),(padding,padding)))
    oh, ow = (h+2*padding-kh)//stride+1, (w+2*padding-kw)//stride+1
    output = np.empty((n, out_channels, oh, ow))
    for r in range(oh):
        for c in range(ow):
            patch = padded[:, :, r*stride:r*stride+kh, c*stride:c*stride+kw]
            output[:, :, r, c] = np.einsum('nchw,ochw->no', patch, kernel)
    if bias is not None:
        output += np.asarray(bias)[None, :, None, None]
    return output
