"""Beam Search
分类：解码
题意：next_log_probs(prefix) 返回词表对数概率；保留 beam_size 个前缀，EOS 停止扩展。
思路：累加对数概率，结束序列也保留在候选池；这里不用长度惩罚。
复杂度：O(T·B·V·(T+log(BV))) 教学实现，含复制与排序。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

def beam_search(next_log_probs, start, eos, beam_size=3, max_steps=20):
    beams = [(tuple(start), 0.0, bool(start and start[-1] == eos))]
    for _ in range(max_steps):
        candidates = []
        for tokens, score, ended in beams:
            if ended:
                candidates.append((tokens, score, True))
            else:
                for token, log_probability in enumerate(next_log_probs(tokens)):
                    candidates.append((tokens + (token,), score + float(log_probability), token == eos))
        candidates.sort(key=lambda item: (-item[1], item[0]))
        beams = candidates[:beam_size]
        if all(item[2] for item in beams):
            break
    return [(list(tokens), score) for tokens, score, _ in beams]
