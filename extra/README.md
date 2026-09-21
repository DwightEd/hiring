# 面经与高频补充 · 51 题

覆盖 Hot100 之外的常见算法以及有明确主题的面经改编。公司归属以公司索引为准，未绑定来源的条目是备考补充，不宣称是某公司的真题。

[返回总目录](../README.md)

## 字符串与数学（16）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [8. 字符串转换整数](../extra/0008_string_to_integer_atoi.py) | 跳过前导空格，读取可选符号与连续数字，截断到有符号 32 位范围。 | O(n) 时间，O(1) 空间 |
| [9. 回文整数](../extra/0009_palindrome_number.py) | 不转字符串，只反转后半数字；末尾为零的非零数直接排除。 | O(log n) 时间，O(1) 空间 |
| [10. 正则表达式匹配](../extra/0010_regular_expression_matching.py) | 完整匹配，点号任意单字符，星号重复前一项；模式保证合法。滚动 DP 枚举使用零次或继续使用。 | O(mn) 时间，O(n) 空间 |
| [43. 字符串相乘](../extra/0043_multiply_strings.py) | 非负十进制数不能整体转 int；按竖式把每对数位贡献加到结果数组。 | O(mn) 时间，O(m+n) 空间 |
| [50. 快速幂](../extra/0050_powx_n.py) | 指数为负时先取倒数，二进制拆分指数；合法输入不会对零取负幂。 | O(log(abs(n)+1)) 时间，O(1) 空间 |
| [69. 整数平方根](../extra/0069_sqrtx.py) | 二分寻找平方不超过 x 的最大整数，不用浮点。 | O(log(x+1)) 算术操作，O(1) 空间 |
| [91. 数字串解码计数](../extra/0091_decode_ways.py) | 1..26 对应字母，零不能单独解码；滚动 DP 考虑一位和两位结尾。 | O(n) 时间，O(1) 空间 |
| [93. 复原 IPv4 地址](../extra/0093_restore_ip_addresses.py) | 数字串分成四段，每段 0..255 且无前导零；按剩余长度剪枝。 | 输出敏感，最多枚举 3^4 个分段；O(n) 输出空间 |
| [151. 翻转单词顺序](../extra/0151_reverse_words_in_a_string.py) | 按空白拆词，逆序连接，并去除多余空格。 | O(n) 时间和空间 |
| [165. 比较版本号](../extra/0165_compare_version_numbers.py) | 按点分隔的各段数值比较，忽略前导零与末尾零段；不把超长段转 int。 | O(m+n) 时间和空间 |
| [179. 最大数](../extra/0179_largest_number.py) | 把非负整数排列成拼接最大值，用 a+b 与 b+a 决定两数顺序。 | O(n log n·L) 时间，O(nL) 空间 |
| [224. 基本计算器](../extra/0224_basic_calculator.py) | 支持整数、空格、加减与括号，含一元负号；栈保存括号外的总和与符号。 | O(n) 时间，O(n) 空间 |
| [402. 移掉 K 位数字](../extra/0402_remove_k_digits.py) | 删除恰好 k 位使非负数最小，单调栈贪心优先删除较大的前位。 | O(n) 时间和空间 |
| [415. 大数加法](../extra/0415_add_strings.py) | 不整体转 int，逆序逐位加法处理进位。 | O(m+n) 时间，O(max(m,n)) 输出空间 |
| [1012. 至少一位重复数字](../extra/1012_numbers_with_repeated_digits.py) | 数位 DP 统计 1..n 中所有数位互异的数，再用 n 减去；前导零不占数字位。 | O(log n·2^10·10) 时间，O(log n·2^10) 空间 |
| [字符种类补集](../extra/character_complement.py) | 返回 a 中出现而 b 中未出现的字符，按首次出现顺序去重；不是多重集合差。 | O(m+n) 期望时间，O(字符集大小) 空间 |

## 链表与数据结构（4）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [92. 指定区间反转链表](../extra/0092_reverse_linked_list_ii.py) | 1-based 区间 left..right 原地反转；不断把后继搬到区间最前面。 | O(n) 时间，O(1) 空间 |
| [143. 重排链表](../extra/0143_reorder_list.py) | 重排为首、尾、次首、次尾；找中点、反转后半、交替合并。 | O(n) 时间，O(1) 空间 |
| [232. 双栈实现队列](../extra/0232_implement_queue_using_stacks.py) | 输入栈只负责追加，输出栈为空时一次搬运全部元素。 | 操作均摊 O(1)，O(n) 空间 |
| [460. LFU 缓存](../extra/0460_lfu_cache.py) | 按访问频率淘汰，同频淘汰最久未用项；频率桶中维护 OrderedDict。 | get/put O(1) 期望，O(capacity) 空间 |

## 二叉树（4）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [103. 二叉树锯齿层序遍历](../extra/0103_binary_tree_zigzag_level_order_traversal.py) | BFS 按层收集，奇数层反转结果，节点处理顺序仍保持从左到右。 | O(n) 时间，O(w) 辅助空间 |
| [110. 平衡二叉树](../extra/0110_balanced_binary_tree.py) | 后序计算高度，任一节点两侧高度差超过一即失败；用显式栈避免深递归。 | O(n) 时间，O(n) 空间 |
| [297. 二叉树序列化](../extra/0297_serialize_and_deserialize_binary_tree.py) | 使用含空节点标记的 BFS 序列；反序列化按同一顺序构造。 | O(n) 时间和空间 |
| [二叉树子结构](../extra/tree_substructure.py) | 非空 B 是否能匹配 A 的某个节点起始的部分结构；B 为空按题型约定返回 False。 | 最坏 O(mn) 时间，O(m+n) 辅助空间 |

## 动态规划（7）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [122. 股票无限次交易](../extra/0122_best_time_to_buy_and_sell_stock_ii.py) | 同时最多持有一股；将所有相邻上涨收益累加。 | O(n) 时间，O(1) 空间 |
| [123. 股票最多两次交易](../extra/0123_best_time_to_buy_and_sell_stock_iii.py) | 维护第一次买卖和第二次买卖四个状态。 | O(n) 时间，O(1) 空间 |
| [221. 最大正方形](../extra/0221_maximal_square.py) | 字符 0/1 网格，dp 为以当前格为右下角的最大边长，依赖左、上、左上最小值。 | O(mn) 时间，O(n) 空间 |
| [309. 股票冷冻期](../extra/0309_best_time_to_buy_and_sell_stock_with_cooldown.py) | 卖出后一天不能买入，维护持股、今天卖出、空仓休息三个状态。 | O(n) 时间，O(1) 空间 |
| [518. 零钱兑换组合数](../extra/0518_coin_change_ii.py) | 面额互异正数且可无限使用；先遍历硬币，再顺序遍历金额，避免计算排列。 | O(amount·种类数) 时间，O(amount) 空间 |
| [714. 股票交易手续费](../extra/0714_best_time_to_buy_and_sell_stock_with_transaction_fee.py) | 无限交易，每次卖出收一次手续费；维护持股和空仓状态。 | O(n) 时间，O(1) 空间 |
| [718. 最长重复子数组](../extra/0718_maximum_length_of_repeated_subarray.py) | 沿两数组的每条对角线连续比较，断开便重置长度。 | O(mn) 时间，O(1) 空间 |

## 图论（5）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [127. 单词接龙](../extra/0127_word_ladder.py) | 每步换一个字母，中间词必须来自字典；双向 BFS 扩展较小边界。 | O(N·L²·26) 上界，计 Python 字符串构造；O(NL) 空间 |
| [210. 课程表顺序](../extra/0210_course_schedule_ii.py) | Kahn 拓扑排序返回任意可行顺序，有环返回空列表。 | O(V+E) 时间和空间 |
| [547. 省份数量](../extra/0547_number_of_provinces.py) | 无向邻接矩阵的连通块数，并查集路径压缩与按大小合并。 | O(n² α(n)) 上界，O(n) 空间 |
| [743. 网络延迟时间](../extra/0743_network_delay_time.py) | 非负权有向图，从起点向所有点传播的最晚到达时间；Dijkstra 用最小堆。 | O((V+E) log(E+1)) 时间，O(V+E) 空间 |
| [1584. 连接所有点的最小费用](../extra/1584_min_cost_to_connect_all_points.py) | 完全图曼哈顿距离，朴素 Prim 不显式保存 n² 条边。 | O(n²) 时间，O(n) 空间；二维几何有更复杂的 O(n log n) 方法 |

## 数组、排序与双指针（12）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [209. 长度最小的子数组](../extra/0209_minimum_size_subarray_sum.py) | 数组全为正，求和至少 target 的最短子数组；满足后尽量收缩窗口。 | O(n) 时间，O(1) 空间 |
| [503. 循环数组下一个更大元素](../extra/0503_next_greater_element_ii.py) | 扫描两遍下标，单调栈只在第一遍入栈，第二遍负责补齐跨边界答案。 | O(n) 时间和空间 |
| [862. 含负数的最短达标子数组](../extra/0862_shortest_subarray_with_sum_at_least_k.py) | 普通滑窗不适用；前缀和配单调队列，淘汰已结算的队首及被新前缀支配的队尾。 | O(n) 时间和空间 |
| [912. 手写堆排序](../extra/0912_sort_an_array.py) | 原地建立最大堆，再将堆顶逐次换到末尾并缩小堆。 | 最坏 O(n log n) 时间，O(1) 辅助空间 |
| [前 K 大或前 K 小](../extra/top_k_numbers.py) | 返回最大/最小 k 个值并按目标顺序排序，重复值保留；小顶堆保留最大 k 个。 | O(n log(k+1)+k log(k+1)) 时间，O(k) 空间 |
| [有序列表公共元素](../extra/sorted_intersection.py) | 两个升序列表输出去重交集；各指针只前进。 | O(m+n) 时间，O(1) 辅助空间，不计输出 |
| [矩形相交面积](../extra/rectangle_overlap.py) | 轴对齐矩形，输入 (x1,y1,x2,y2)，x1<=x2、y1<=y2；返回相交面积而非 IoU。 | O(1) 时间和空间 |
| [左侧全小右侧全大的元素](../extra/partition_pivots.py) | 找所有严格大于全部左侧且小于全部右侧的元素下标；端点空侧条件视为成立。 | O(n) 时间和空间 |
| [手写三路快速排序](../extra/quicksort.py) | 随机枢轴三路分区，先处理小区间、大区间压栈，控制栈高度。 | O(n log n) 期望、O(n²) 最坏时间，O(log n) 栈空间 |
| [和为 K 的最长子数组](../extra/max_length_sum_k.py) | 前缀和记录最早位置 | O(n) 时间空间 |
| [优化冒泡排序](../extra/bubble_sort.py) | 记录最后交换位置 | 最好 O(n)，最坏 O(n²)，O(1) 空间 |
| [加权热度去重 Top K](../extra/weighted_unique_topk.py) | 每个 ID 保留最高分后用堆选 K | O(nd+u log(k+1)+k log k) 时间 |

## Agent 与数据处理（3）

| 题目 / 代码 | 核心思路 | 复杂度 |
|---|---|---|
| [工具调用日志统计](../extra/tool_log_statistics.py) | 哈希计数；并列按首次出现 | O(n+m) 时间，O(m) 空间 |
| [按城市汇总订单](../extra/city_order_totals.py) | 整数分累计 | O(n) 时间，O(c) 空间 |
| [流式 JSON 分帧](../extra/stream_json.py) | 状态机处理括号和字符串转义 | O(n) 时间，O(最长帧) 工作空间 |
