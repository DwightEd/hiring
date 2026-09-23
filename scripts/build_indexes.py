"""从 catalog 生成可点击的分类索引；新增题后运行 python scripts/build_indexes.py。"""
import json
from collections import defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(name):
    return json.loads((ROOT/'catalog'/(name+'.json')).read_text())


def escape(text):
    return str(text).replace('|','\\|').replace('\n',' ')


def write_problem_index(group,title,intro):
    groups=defaultdict(list)
    for row in read(group):groups[row['category']].append(row)
    lines=[f'# {title}','',intro,'','[返回总目录](../README.md)','']
    for category,rows in groups.items():
        lines += [f'## {category}（{len(rows)}）','','| 题目 / 代码 | 核心思路 | 复杂度 |','|---|---|---|']
        for row in rows:
            label=(str(row['id'])+'. ' if isinstance(row['id'],int) else '')+row['title']
            complexity=('时间 '+row['time']+'；空间 '+row['space']) if group=='hot100' else row['complexity']
            lines.append(f"| [{label}](../{row['path']}) | {escape(row['idea'])} | {escape(complexity)} |")
        lines += ['']
    (ROOT/group/'README.md').write_text('\n'.join(lines).rstrip()+'\n')


def write_companies():
    sources={row['id']:row for row in read('sources')}
    groups=defaultdict(list)
    for row in read('company_questions'):groups[row['company']].append(row)
    lines=['# 公司面经 → 编程题索引','','这里记录公开页面或已提供题面中出现的编程主题。面经是网友自述或整理，不代表公司官方题库；每项来源的核对日期见 catalog/sources.json。','',
           '同一题不重复计数，下面直接引用 Hot100、补充题、AI 模块或公司专属题面与实现。主题不完整的题标为改编；补充的输入约定写在代码文件头。未披露公司、非 AI 岗也分别标明。','',
           '[华为三道笔试题与样例](huawei/README.md) · [拼多多四题完整题面与代码](pinduoduo/README.md) · [来源清单与待补题](../docs/SOURCES.md) · [返回总目录](../README.md)','']
    for company,rows in groups.items():
        lines += [f'## {company}','','| 岗位 / 时间 | 题目与解答 | 来源 / 收录状态 |','|---|---|---|']
        for row in rows:
            source=sources[row['source_id']]
            reference=f"[{source['title']}]({source['url']})" if source['url'] else source['title']+'（已提供截图）'
            code='、'.join(f"[{Path(p).stem}](../{p})" for p in row['paths'])
            lines.append(f"| {row['role']} / {row['period']} | {row['title']}；{code} | {reference}；{row['status']} |")
            if row['notes']:lines.append(f"| 说明 | {row['notes']} | |")
        lines += ['']
    (ROOT/'companies/README.md').write_text('\n'.join(lines).rstrip()+'\n')


if __name__=='__main__':
    write_problem_index('hot100','LeetCode Hot100 · 100/100','分类与题号以 2026-09-21 力扣官方 Hot100 学习计划为准；每个文件含题意、思路、时间/空间复杂度与原题链接。')
    write_problem_index('extra','面经与高频补充 · 51 题','覆盖 Hot100 之外的常见算法以及有明确主题的面经改编。公司归属以公司索引为准，未绑定来源的条目是备考补充，不宣称是某公司的真题。')
    write_problem_index('ai','AI 算法手撕 · 36 模块','NumPy / 标准库实现：数值稳定性、维度、梯度、并列规则写在文件头。每个模块计一次，前向和反向不重复计数。运行测试需安装 requirements.txt。')
    write_companies()
