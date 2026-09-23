# 秋招 Python 算法手撕题库

**LeetCode 官方 Hot100：100/100。** 按官方 17 类整理，附 Python 解答、中文思路和复杂度。另收录面经补充算法、AI 算子/模型手撕，以及华为 AI、拼多多笔试题。

收录更新：**2026-09-23**。主清单共 **196 道题目/模块**（原 190 项加拼多多 4 题、FFN 与 Transformer 2 模块；同题多语言实现不重复计数），公司索引引用已有题目时不重复计数。公开面经是持续增长的开放集合，本仓库是可追溯的收录快照，不声称穷尽所有招聘/讨论网站。

| 入口 | 数量 | 内容 |
|---|---:|---|
| [Hot100 分类目录](hot100/README.md) | 100 | 哈希、双指针、滑窗、链表、树、图、回溯、二分、堆、贪心、DP 等 17 类 |
| [补充题分类目录](extra/README.md) | 51 | 字符串运算、缓存、股票、最短路、数位 DP、排序、Agent 日志与流式解析等 |
| [AI 算法分类目录](ai/README.md) | 38 | Softmax、损失、归一化、Attention/MHA/GQA、FFN、完整 Transformer 前向、RoPE、LoRA 等 |
| [华为 AI 笔试](companies/huawei/README.md) | 3 | 全局位与窗口注意力、流水线最小峰值负载、MoE 容量路由 |
| [拼多多 2026-09-22 截图题](companies/pinduoduo/README.md) | 4 | 完整整理题面、I/O、约束、样例、Python；括号题另附 C++17 |
| [按公司查题](companies/README.md) | 复用上述实现 | 华为、字节、阿里、百度、美团、小红书、京东、快手、地平线、58 同城、拼多多等 |

## 开始练习

建议 Python 3.10+；已在 Python 3.12 环境验证。从仓库根目录运行：

```bash
# Hot100、补充题和华为题仅依赖标准库。
python -m unittest tests.test_hot100 tests.test_extra tests.test_huawei -v

# 新增拼多多题：24 项测试；有 g++ 时同时验证 C++ 备选。
python -m unittest discover -s tests -p test_pinduoduo.py -v

# AI 数值模块依赖 NumPy。
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v

# 按 LeetCode 题号试运行普通数组/字符串题。
python practice.py 1 --args '[[2,7,11,15],9]'
python practice.py 5 --args '["babad"]'
python practice.py 415 --args '["999","1"]'

# 手写多头注意力 + FFN + 完整 Encoder–Decoder 前向。
python transformer_demo.py
python transformer_demo.py --d-model 16 --heads 4 --d-ff 64 --layers 2 --seed 7
python -m unittest tests.test_ai tests.test_transformer -v
```

节点题和设计类（树、链表、LRU、Trie、最小栈等）需要构造对象，完整用例在 `tests/test_hot100.py` 与 `tests/test_extra.py`。AI 模块在仓库根目录通过 `from ai.attention import attention` 等方式导入；单独直接执行函数定义文件不会自动打印结果。

[Transformer 中文教程](docs/TRANSFORMER.md) 逐步解释 Q/K/V、拆头合头、FFN、残差、位置编码、padding 与因果遮罩。演示使用 NumPy 和随机权重，支持完整前向，不包含训练循环。Windows 若因系统默认 GBK 读取题库 JSON 报错，可使用 `python -X utf8 -m unittest discover -s tests -v`。

## 怎么刷

1. 先按 [Hot100](hot100/README.md) 的分类走一遍；每题先写朴素思路，再读高效解法。
2. 目标是算法/大模型岗位时，同步练 [AI 手撕](ai/README.md)，能解释张量维度、归一化轴、掩码和梯度。
3. 面试前查 [公司索引](companies/README.md)，再做 [华为 ACM 输入输出](companies/huawei/README.md)。同一题换了描述，也要认出它的状态、不变量与边界。
4. Python 不熟时，先看 [语法与手撕速查](docs/PYTHON.md)：排序键、元组、堆、集合、输入输出和节点对象。

## 解法与验证

每份 Hot100 文件包含题意摘要、原题链接、思路、时间和空间复杂度。优先采用标准高效解法，包含原地链表归并、Manacher、随机三路快速选择和空间压缩 DP。随机期望复杂度、数论前提及教学实现的取舍见 [复杂度说明](docs/COMPLEXITY.md)。

2026-09-23 增补 Transformer 后，运行 `python -X utf8 -m unittest discover -s tests -v`：**228 项测试通过**，C++ 对照测试组因环境未安装 `g++` 跳过。新增验证包含 MHA/FFN 手算值、Encoder/Decoder 残差与 Post-LN、因果与 padding 隔离、跨样本隔离、全遮罩稳定性及演示入口；默认演示的 logits 形状为 `[2,3,32]`。

初始 2026-09-21 快照记录 **192 项 unittest 测试通过**，用例覆盖当时的 190 份解答；其中包含随机小数据对照、2,500 层深树、节点身份/链表恢复、华为精确分段穷举、数值稳定性与中心差分梯度检查。这是本地验证结果，未声称已逐题提交官方判题器。

本次新增拼多多题的 **24 项测试通过**，含穷举、随机对照、I/O 和 C++ 对照；未重新运行原有全量测试。括号题 Python 在本机完整规模随机混合操作中约 5.6 秒，不能承诺满足截图中的 1 秒时限；另附 C++17 同算法版本。详见 [验证范围与计时](companies/pinduoduo/VALIDATION.md)。

## 来源与维护

[来源清单及待补题](docs/SOURCES.md) 区分官方题单、公开面经、用户提供题面和通用备考练习。公司/年份/岗位仅在可读来源明确时标注；原帖省略的输入规则会明确写成“本仓库练习约定”。通常保留简要题意和自主实现；本次按用户要求为拼多多截图题整理完整规则、输入输出与约束，无法从截图恢复的样例明确注明。原始完整面经请访问作者链接。

题目元数据在 `catalog/`；新增条目后补测试，再运行：

```bash
python scripts/build_indexes.py
python -m unittest discover -s tests -v
```

`catalog/company_questions.json` 负责公司与代码的映射，`catalog/sources.json` 记录来源性质、核对日期和已知缺失。对于原帖说“题忘了”或条件不足的题，保留待补记录，不用猜测的代码冒充原题答案。
