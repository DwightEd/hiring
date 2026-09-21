"""二分类 Focal Loss。输入同形状 logits 与 0/1 标签；默认 mean reduction。
FL=-alpha_t*(1-p_t)^gamma*log(p_t)，在 log 域计算避免 log(0)。
时间/空间 O(N)。公开作者社招面经提到手写本题，未标具体公司；见来源索引。
"""
import numpy as np


def focal_loss(logits, labels, alpha=0.25, gamma=2.0):
    x, y = np.asarray(logits, dtype=float), np.asarray(labels, dtype=float)
    signed = (2*y-1)*x
    log_pt = -np.logaddexp(0, -signed)
    alpha_t = np.where(y == 1, alpha, 1-alpha)
    return float(np.mean(-alpha_t * (-np.expm1(log_pt))**gamma * log_pt))
