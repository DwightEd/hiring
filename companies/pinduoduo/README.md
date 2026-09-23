# 拼多多 2026-09-22 笔试截图题：完整题面与实现

本目录依据用户提供的四张截图整理。公司、日期沿用截图标题，岗位未展示；未独立核实为公司官方发布，也没有把来源不明的网页补成“官方题面”。

每题都有完整整理的规则、输入输出、约束、解法、复杂度和可直接提交格式的程序。**截图未拍全的原样例不会凭空补写**：第一题补充输出明确注明由题意计算；第三、四题给出自编完整样例。原截图不上传仓库。

| 顺序 | 完整题面 | Python | 核心算法 | 时间复杂度 |
|---|---|---|---|---|
| 1 | [货架最少搬运次数](01_shelf_moves.md) | [shelf_moves.py](shelf_moves.py) | 连续等值段计数 | O(n) |
| 2 | [多多字符串](02_duoduo_string.md) | [duoduo_string.py](duoduo_string.py) | 全部 a + 中间区间 #b-#a 的最大收益 | O(n) |
| 3 | [果园最小收集边长](03_orchard_square.md) | [orchard_square.py](orchard_square.py) | 二分答案 + x 滑窗 + y 离散化 + 区间加最大值 | O(n log n log U) |
| 4 | [括号串翻转与合法查询](04_bracket_queries.md) | [bracket_queries.py](bracket_queries.py) | 前缀和极值 + 懒标记线段树 | 建树 O(n)，每次 O(log n) |

`U` 是覆盖所有苹果的边长，不超过 10^9。四题都仅依赖 Python 标准库。第四题另有 [C++17 实现](bracket_queries.cpp)，与 Python 使用相同的数学状态和区间翻转规则。

## 直接运行

从仓库根目录执行，`input.txt` 按对应题面填写：

```bash
python companies/pinduoduo/shelf_moves.py < input.txt
python companies/pinduoduo/duoduo_string.py < input.txt
python companies/pinduoduo/orchard_square.py < input.txt
python companies/pinduoduo/bracket_queries.py < input.txt

# 正确性测试，不会下载数据或访问网络。
python -m unittest discover -s tests -p test_pinduoduo.py -v

# 第四题严格时限备选，编译产物放在 /tmp，不写进仓库。
g++ -O2 -std=c++17 companies/pinduoduo/bracket_queries.cpp -o /tmp/pdd_brackets
/tmp/pdd_brackets < input.txt
```

## 四个关键点

第一题统计的是连续段，不是不同数字数目；货架不会被删除后拼起来。第二题允许删除字符，因此求的是子序列，不是最长连续子串。第三题覆盖完整单元格，边长是坐标极差加 1，离散化下标不能替代真实距离。第四题翻转的是括号种类而非顺序，合法性必须同时检查总和为 0 和所有前缀和非负。

## 验证与时限

本次新增 24 项测试通过，含随机/穷举对照及全部 CLI；原有题库未重跑全量测试。第四题 Python 在本机 n=q=200000 的一组随机混合操作中约需 5.6 秒，截图标注 1000 ms，因此不能保证 Python 满足原平台时限。C++17 同规模测得约 0.19 秒，也不是官方评测保证。详细环境、计时口径和测试范围见 [VALIDATION.md](VALIDATION.md)。

[公司总索引](../README.md) · [返回项目首页](../../README.md)
