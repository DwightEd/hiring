# 公司面经 → 编程题索引

这里记录公开页面或已提供题面中出现的编程主题。面经是网友自述或整理，不代表公司官方题库；核对日期为 2026-09-21。

同一题只保留一份解答，下面直接引用 Hot100、补充题或 AI 模块。主题不完整的题标为改编；补充的输入约定写在代码文件头。未披露公司、非 AI 岗也分别标明。

[华为三道笔试题与样例](huawei/README.md) · [来源清单与待补题](../docs/SOURCES.md) · [返回总目录](../README.md)

## 华为

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| AI 笔试 / 2026-09-18 | 全局位与窗口注意力；[global_window_attention](../companies/huawei/global_window_attention.py) | 华为 2026-09-18 AI 笔试 P5467 / P5468（已提供截图）；题意明确；CLI 输入顺序采用练习约定 |
| 说明 | 候选并集、正分过滤、同分小下标、整数加权求和；无 softmax。 | |
| AI 笔试 / 2026-09-18 | 流水线并行最小峰值负载；[pipeline_partition](../companies/huawei/pipeline_partition.py) | 华为 2026-09-18 AI 笔试 P5467 / P5468（已提供截图）；题意明确，按标准题实现 |
| AI 笔试 / 2026-07-24 | MoE Top-K 容量路由；[moe_capacity_routing](../companies/huawei/moe_capacity_routing.py) | [华为 AI 2026-07-24 笔试回忆](https://www.nowcoder.com/discuss/914337978896384000)；题意明确，按标准题实现 |
| 大模型算法 / 2026-09-17 | 和为 K 的最长子数组；[max_length_sum_k](../extra/max_length_sum_k.py) | [华为大模型算法岗面经-04](https://www.nowcoder.com/discuss/931707110344130560)；题意明确，按标准题实现 |
| 海思人工智能算法 / 2020届 | 指定区间反转链表；[0092_reverse_linked_list_ii](../extra/0092_reverse_linked_list_ii.py) | [作者 2020 届计算机视觉秋招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/4-计算机视觉岗2020届秋招面经.md)；题意明确，按标准题实现 |

## 字节跳动

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| Agent 开发 / 2026-09 | 树的子结构；有序 List 交集；[tree_substructure](../extra/tree_substructure.py)、[sorted_intersection](../extra/sorted_intersection.py) | [字节 Agent 秋招一面](https://www.nowcoder.com/discuss/929731481189044224)；主体题意明确；交集采用集合语义 |
| 说明 | 原帖未说明重复次数，本练习输出去重后的相同元素；无限流追问见待补说明。 | |
| AI Agent 开发 / 2026-09-20 | 工具成功率与最多失败工具；[tool_log_statistics](../extra/tool_log_statistics.py) | [9.20 字节 AI Agent 开发一面](https://www.nowcoder.com/discuss/931682493218947072)；主题改编，接口与并列规则见文件头 |

## 阿里巴巴

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 计算机视觉算法 / 2019届 | N 个数中最大的 K 个数；[top_k_numbers](../extra/top_k_numbers.py) | [作者 2019 届计算机视觉实习面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/1-计算机视觉岗2019届实习面经.md)；题意明确，按标准题实现 |

## 百度

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 大模型算法 / 2026-09 | 最长公共子序列；最长回文子串；[1143_longest_common_subsequence](../hot100/16_多维动态规划/1143_longest_common_subsequence.py)、[0005_longest_palindromic_substring](../hot100/16_多维动态规划/0005_longest_palindromic_substring.py) | [百度大模型算法岗一二面面经](https://www.nowcoder.com/feed/main/detail/15b32d64325d4c968096eba29076d75d)；题意明确，按标准题实现 |

## 美团

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| AI 应用开发 / 2026-09-14 | 最长无重复子串；[0003_longest_substring_without_repeating_characters](../hot100/03_滑动窗口/0003_longest_substring_without_repeating_characters.py) | [美团 AI 应用开发一面](https://www.nowcoder.com/discuss/931678729829384192)；题意明确，按标准题实现 |

## 小红书

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 大模型算法 / 2026-09 | 链表两两交换；[0024_swap_nodes_in_pairs](../hot100/07_链表/0024_swap_nodes_in_pairs.py) | [小红书大模型算法面经](https://www.nowcoder.com/discuss/931682969507332096)；题意明确，按标准题实现 |
| 大模型算法笔试 / 2026-09 | 加权热度排序后去重 Top N；[weighted_unique_topk](../extra/weighted_unique_topk.py) | [小红书大模型算法面经](https://www.nowcoder.com/discuss/931682969507332096)；主题改编，字段、权重与去重规则见文件头 |

## 京东

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 算法工程师笔试 / 2026-09 | 按城市汇总订单金额；[city_order_totals](../extra/city_order_totals.py) | [京东算法工程师笔试与一面](https://www.nowcoder.com/discuss/931679472032444416)；列表摘要主题改编 |
| 说明 | 整数分、退款、重复记录的处理均为本仓库约定。 | |

## 快手

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| Agent 开发 / 2026-09 | 流式 JSON 解析/半包拼接；[stream_json](../extra/stream_json.py) | [快手 Agent 开发一面](https://www.nowcoder.com/discuss/931679347587444736)；主题改编，限定顶层对象或数组 |
| 说明 | 按字符分块；若输入是字节流，需要增量 UTF-8 解码器。 | |

## 地平线

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 智能驾驶算法实习 / 2019届 | 字符类型补集；重复数字计数；矩形相交面积；Softmax 前后向；[character_complement](../extra/character_complement.py)、[1012_numbers_with_repeated_digits](../extra/1012_numbers_with_repeated_digits.py)、[rectangle_overlap](../extra/rectangle_overlap.py)、[softmax](../ai/softmax.py) | [作者 2019 届计算机视觉实习面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/1-计算机视觉岗2019届实习面经.md)；题意明确；矩形按面积实现 |
| 说明 | 原帖把重叠面积与 IoU 混称，按题目明确要求实现面积；IoU 另见 AI 模块。 | |
| 计算机视觉算法 / 2020届 | 二叉树右视图；[0199_binary_tree_right_side_view](../hot100/08_二叉树/0199_binary_tree_right_side_view.py) | [作者 2020 届计算机视觉秋招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/4-计算机视觉岗2020届秋招面经.md)；题意明确，按标准题实现 |

## 58同城

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 机器学习算法 / 2020届 | 手写 NMS；[iou_nms](../ai/iou_nms.py) | [作者 2020 届计算机视觉秋招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/4-计算机视觉岗2020届秋招面经.md)；题意明确，按标准题实现 |

## 瓜子二手车

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 机器学习算法 / 2020届 | 重复有序数组最左下标；不转字符串判断回文整数；[0034_find_first_and_last_position_of_element_in_sorted_array](../hot100/11_二分查找/0034_find_first_and_last_position_of_element_in_sorted_array.py)、[0009_palindrome_number](../extra/0009_palindrome_number.py) | [作者 2020 届计算机视觉秋招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/4-计算机视觉岗2020届秋招面经.md)；题意明确，按标准题实现 |
| 说明 | LC34 返回 [首,尾]；取结果第 0 项即首下标，不存在时为 -1。 | |

## 涂鸦移动

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 软件开发（非 AI 岗） / 2020届 | Top K；三数之和；[top_k_numbers](../extra/top_k_numbers.py)、[0015_3sum](../hot100/02_双指针/0015_3sum.py) | [作者 2020 届计算机视觉秋招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/4-计算机视觉岗2020届秋招面经.md)；题意明确，按标准题实现 |

## 未披露公司

| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |
|---|---|---|
| 视觉算法社招 / 2021 | Soft-NMS；Focal Loss；Softmax；[soft_nms](../ai/soft_nms.py)、[focal_loss](../ai/focal_loss.py)、[softmax](../ai/softmax.py) | [作者 2021 视觉算法社招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/5-视觉算法岗2021年社招面经.md)；题意明确，按标准题实现 |
| 视觉算法社招 / 2021 | 二分、反转链表、最小栈、回文子串、最小 K 数、冒泡、枢轴位置、快排、无重复子串、N 皇后、第 K 大；[0035_search_insert_position](../hot100/11_二分查找/0035_search_insert_position.py)、[0206_reverse_linked_list](../hot100/07_链表/0206_reverse_linked_list.py)、[0155_min_stack](../hot100/12_栈/0155_min_stack.py)、[0005_longest_palindromic_substring](../hot100/16_多维动态规划/0005_longest_palindromic_substring.py)、[top_k_numbers](../extra/top_k_numbers.py)、[bubble_sort](../extra/bubble_sort.py)、[partition_pivots](../extra/partition_pivots.py)、[quicksort](../extra/quicksort.py)、[0003_longest_substring_without_repeating_characters](../hot100/03_滑动窗口/0003_longest_substring_without_repeating_characters.py)、[0051_n_queens](../hot100/10_回溯/0051_n_queens.py)、[0215_kth_largest_element_in_an_array](../hot100/13_堆/0215_kth_largest_element_in_an_array.py) | [作者 2021 视觉算法社招面经](https://github.com/harleyszhang/cv_note/blob/master/interview_summary/5-视觉算法岗2021年社招面经.md)；题意明确，按标准题实现 |
| 说明 | LC35 是 lower_bound；要做精确二分须检查结果下标是否在界内且对应值等于目标。最小 K 数设置 largest=False。 | |
