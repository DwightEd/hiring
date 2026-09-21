# 华为 AI 笔试

[返回公司目录](../README.md) · [返回总目录](../../README.md)

| 题目 | 来源 | 关键规则 |
|---|---|---|
| [全局位与窗口注意力](global_window_attention.py) | 用户此前提供的 2026-09-18 AI 题面 P5467 | 全局位与窗口取并集；点积严格为正；Top T 同分小下标；整数加权累加，无 softmax |
| [流水线最小峰值负载](pipeline_partition.py) | 用户此前提供的 2026-09-18 AI 题面 P5468 | 按原顺序恰好 K 个非空连续段，最小化最大段和 |
| [MoE Top-K 容量路由](moe_capacity_routing.py) | [2026-07-24 公开回忆](https://www.nowcoder.com/discuss/914337978896384000) | 每个 token 固定 Top K；同分小专家下标；容量满直接丢弃，不重新选专家 |

下方注意力、流水线样例是本仓库自拟练习；MoE 样例对应公开回忆中的可读样例。所有命令从仓库根目录运行。

## 1. 全局位与窗口注意力

```bash
python companies/huawei/global_window_attention.py < input.txt
```

练习输入格式：`L D G W T`，接着 G 个 **0 起始**全局下标，再接 Q、K、V 三个 L×D 矩阵。截图只显示了首行格式，后续矩阵与下标的读取先后未展示；这里的 CLI 顺序是练习约定，若原平台顺序不同，只调整 `solve()`，核心算法不变。

`input.txt`：

```text
2 1 1 1 1
0
1
1
1
1
2
9
```

Q 和 K 都是两行 `[1]`，V 的两行分别是 `[2]`、`[9]`。两位置都能看到 0、1，分数相同而 T=1，故选择下标 0。输出：

```text
2
2
```

不能把集合并集写成简单列表相加，交叠位置会被重复计入。堆保存 `(score, -index)`，以保证堆顶始终是已选项中最差的一项。Python 整数不会因大点积溢出固定 32 位范围。

## 2. 流水线最小峰值负载

```bash
python companies/huawei/pipeline_partition.py < input.txt
```

输入：

```text
5 2
7 2 5 10 8
```

输出：

```text
18
```

可切成 `[7,2,5]` 和 `[10,8]`，峰值为 18。API `split_exactly_k(times, k)` 还能返回分段的左闭右开区间。

**为什么可行性判断写“段数 ≤ K”，题目却是“恰好 K 段”？** 给定峰值上限，贪心得到的是最少段数。如果它不超过 K，因为耗时非负、K≤N，就能继续拆分已有非空段；拆开后的段和不会增大，最终一定达到恰好 K 段。负数输入不满足这一证明，代码会拒绝。

## 3. MoE 容量路由

```bash
python companies/huawei/moe_capacity_routing.py < input.txt
```

输入首行为 `N E K C`，之后 N 行、每行 E 个分数：

```text
4 3 2 2
1 5 4
8 1 2
3 6 5
2 7 9
```

输出第一行是专家负载平方和，第二行是每个专家的负载：

```text
9
1 2 2
```

这里不是 softmax 加权输出，也不是负载均衡损失的训练实现；严格执行题目规定的容量计数过程。
