"""Gaussian Soft-NMS：每轮保留当前最高分，再按 exp(-IoU²/sigma) 衰减剩余分数。
输入连续 xyxy 框，返回原始下标与衰减后分数；低于 minimum 的框丢弃，平分先小下标。
时间 O(N²)，额外 O(N)。sigma>0。来源见作者 2021 社招面经，未指定公司。
"""
import numpy as np
from ai.iou_nms import iou


def soft_nms(boxes, scores, sigma=0.5, minimum=1e-3):
    if sigma <= 0:
        raise ValueError('sigma 必须为正')
    boxes, scores = np.asarray(boxes, dtype=float), np.asarray(scores, dtype=float).copy()
    remaining, result = list(range(len(scores))), []
    while remaining:
        current = min(remaining, key=lambda i: (-scores[i], i))
        if scores[current] < minimum:
            break
        result.append((current, float(scores[current])))
        remaining.remove(current)
        overlap = iou(boxes[current], boxes[remaining])
        scores[remaining] *= np.exp(-overlap**2 / sigma)
    return result
