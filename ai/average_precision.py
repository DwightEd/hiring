"""Average Precision
分类：评估指标
题意：二分类标签与置信分数，按相同分数组同时更新阈值；无正例返回 0。
思路：AP=sum(召回增量×当前精确率)，不把梯形 PR 面积误当 AP。
复杂度：O(n log n) 时间，O(n) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

def average_precision(labels, scores):
    positives = sum(labels)
    if positives == 0:
        return 0.0
    rows = sorted(zip(scores, labels), reverse=True)
    tp = count = i = 0
    answer = 0.0
    while i < len(rows):
        j, added = i, 0
        while j < len(rows) and rows[j][0] == rows[i][0]:
            added += rows[j][1]
            j += 1
        tp += added
        count += j - i
        answer += added / positives * tp / count
        i = j
    return answer
