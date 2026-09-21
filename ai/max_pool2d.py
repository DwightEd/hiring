"""最大池化前向与反向
分类：计算机视觉
题意：NCHW 输入，整数窗口和步长，不补零；反向将梯度加到首次最大值处。
思路：重叠窗口反向必须累加，不能直接覆盖。
复杂度：O(NC·HoWo·k²) 时间，缓存 O(NC·HoWo)。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def max_pool2d(x, size=2, stride=2):
    n, c, h, w = x.shape
    oh, ow = (h-size)//stride+1, (w-size)//stride+1
    output, indices = np.empty((n,c,oh,ow)), np.empty((n,c,oh,ow), dtype=int)
    for r in range(oh):
        for col in range(ow):
            patch = x[:,:,r*stride:r*stride+size,col*stride:col*stride+size].reshape(n,c,-1)
            indices[:,:,r,col] = patch.argmax(axis=-1)
            output[:,:,r,col] = patch.max(axis=-1)
    return output, (x.shape, indices, size, stride)

def backward(grad, cache):
    shape, indices, size, stride = cache
    dx = np.zeros(shape)
    for n, c, r, col in np.ndindex(grad.shape):
        offset = indices[n,c,r,col]
        dx[n,c,r*stride+offset//size,col*stride+offset%size] += grad[n,c,r,col]
    return dx
