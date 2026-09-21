"""简化 BPE 训练和编码
分类：NLP
题意：输入词到频数映射，字符起始，按相邻 token 对的加权频次合并；不跨词。
思路：每轮合并最频繁一对，同频按字典序；编码严格重放合并规则。
复杂度：O(merges·总语料 token 数) 的基础实现；非生产 tokenizer。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

from collections import Counter

def merge_pair(tokens, pair):
    output, index = [], 0
    while index < len(tokens):
        if index+1 < len(tokens) and (tokens[index], tokens[index+1]) == pair:
            output.append(tokens[index] + tokens[index+1])
            index += 2
        else:
            output.append(tokens[index])
            index += 1
    return tuple(output)

def train(word_counts, num_merges):
    vocabulary = {tuple(word): count for word, count in word_counts.items()}
    rules = []
    for _ in range(num_merges):
        counts = Counter()
        for tokens, count in vocabulary.items():
            for pair in zip(tokens, tokens[1:]):
                counts[pair] += count
        if not counts:
            break
        pair = min(counts, key=lambda p: (-counts[p], p))
        new = Counter()
        for tokens, count in vocabulary.items():
            new[merge_pair(tokens, pair)] += count
        vocabulary = new
        rules.append(pair)
    return rules

def encode(word, rules):
    tokens = tuple(word)
    for pair in rules:
        tokens = merge_pair(tokens, pair)
    return list(tokens)
