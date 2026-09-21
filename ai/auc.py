"""ROC AUC
分类：评估指标
题意：labels 为 0/1，scores 越大越偏正类；单一类别时抛出 ValueError。
思路：升序分数组：每个正例胜过所有较低分负例，并与同分负例各计半胜。
复杂度：O(n log n) 时间，O(n) 空间。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

def roc_auc(labels, scores):
    ordered = sorted(zip(scores, labels))
    positives, negatives = sum(labels), len(labels) - sum(labels)
    if not positives or not negatives:
        raise ValueError('AUC 需要正负两类')
    wins, lower_negatives, i = 0.0, 0, 0
    while i < len(ordered):
        j, pos, neg = i, 0, 0
        while j < len(ordered) and ordered[j][0] == ordered[i][0]:
            pos += ordered[j][1] == 1
            neg += ordered[j][1] == 0
            j += 1
        wins += pos * (lower_negatives + neg / 2)
        lower_negatives += neg
        i = j
    return wins / (positives * negatives)
