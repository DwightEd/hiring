"""按加权热度排序、按笔记 ID 去重、返回前 k 条。

来源主题：小红书面经 https://www.nowcoder.com/discuss/931682969507332096
原帖未给权重、字段和并列规则。本仓库练习约定：每行 (ID, 特征向量)；
热度为点积；同 ID 保留最高热度记录；同分保持输入顺序；返回 (ID, 热度)。
先去重再选前 k 与全量排序后去重等价，避免排序所有重复记录。
时间 O(nd + u log(k+1) + k log k)，空间 O(u+k)，u 为不同 ID 数。
"""
from heapq import nlargest


def weighted_unique_topk(rows, weights, k):
    if k <= 0:
        return []
    best = {}
    for index, (note_id, features) in enumerate(rows):
        if len(features) != len(weights):
            raise ValueError("特征数与权重数不一致")
        score = sum(x * w for x, w in zip(features, weights))
        if note_id not in best or score > best[note_id][0]:
            best[note_id] = (score, -index)
    selected = nlargest(k, best, key=best.get)
    return [(note_id, best[note_id][0]) for note_id in selected]
