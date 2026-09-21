"""IoU 与 NMS
分类：计算机视觉
题意：boxes 为 N×4 的连续坐标 xyxy，scores 为 N；IoU 大于阈值的框被抑制。
思路：贪心保留最高分框，删除与之过度重叠的框；坐标面积不加一。
复杂度：NMS 最坏 O(N²)，O(N) 辅助空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def iou(box, boxes):
    box, boxes = np.asarray(box, dtype=float), np.asarray(boxes, dtype=float)
    size = np.maximum(0, np.minimum(box[2:], boxes[..., 2:]) - np.maximum(box[:2], boxes[..., :2]))
    intersection = np.prod(size, axis=-1)
    area = np.prod(np.maximum(0, box[2:] - box[:2]))
    areas = np.prod(np.maximum(0, boxes[..., 2:] - boxes[..., :2]), axis=-1)
    union = area + areas - intersection
    return np.divide(intersection, union, out=np.zeros_like(intersection), where=union > 0)

def nms(boxes, scores, threshold=0.5):
    boxes = np.asarray(boxes, dtype=float)
    order = np.argsort(-np.asarray(scores), kind='stable')
    kept = []
    while len(order):
        current = order[0]
        kept.append(int(current))
        order = order[1:]
        order = order[iou(boxes[current], boxes[order]) <= threshold]
    return kept
