"""PPO、DPO 与 GRPO 组内优势
分类：强化学习
题意：PPO 输入新旧动作 logprob 与优势；DPO 输入策略/参考模型的偏好对序列 logprob；GRPO 输入分组奖励。
思路：PPO 取 clipped surrogate 的较小者；DPO 对相对偏好 margin 做 log-sigmoid；组内标准化奖励。
复杂度：O(N) 时间和空间；实现的是核心目标，非完整训练器。
来源性质：通用算法手撕练习；具体公司出处仅以 companies/README.md 的映射为准。
"""

import numpy as np

def ppo_loss(new_logp, old_logp, advantage, clip=0.2):
    ratio = np.exp(np.asarray(new_logp) - np.asarray(old_logp))
    advantage = np.asarray(advantage)
    return float(-np.minimum(ratio*advantage, np.clip(ratio, 1-clip, 1+clip)*advantage).mean())

def dpo_loss(policy_chosen, policy_rejected, ref_chosen, ref_rejected, beta=0.1):
    margin = beta * ((np.asarray(policy_chosen)-policy_rejected) - (np.asarray(ref_chosen)-ref_rejected))
    return float(np.logaddexp(0, -margin).mean())

def group_advantage(rewards, eps=1e-8):
    rewards = np.asarray(rewards, dtype=float)
    return (rewards-rewards.mean(axis=-1, keepdims=True))/(rewards.std(axis=-1, keepdims=True)+eps)
