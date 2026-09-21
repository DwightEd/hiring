"""按题号调用普通 LeetCode 方法；树、链表与设计类请参照 tests 构造对象。"""
import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('id',type=int,help='LeetCode 题号，例如 1、15、415')
    parser.add_argument('--args',required=True,help='JSON 参数数组，例如 [[2,7,11,15],9]')
    options=parser.parse_args()
    rows=[]
    for group in ['hot100','extra']:
        rows.extend(json.loads((ROOT/'catalog'/(group+'.json')).read_text()))
    row=next((r for r in rows if r['id']==options.id),None)
    if row is None:parser.error('未收录该题号')
    if row.get('category') in {'链表','二叉树'} or options.id in {92,103,110,143,297}:
        parser.error('节点/缓存题请参照 tests/test_hot100.py 或 tests/test_extra.py 构造输入')
    spec=importlib.util.spec_from_file_location('practice_solution',ROOT/row['path'])
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    if not hasattr(module,'Solution'):parser.error('设计类题请参照 tests 中的调用示例')
    names=[name for name in vars(module.Solution) if not name.startswith('_')]
    if len(names)!=1:parser.error('请直接调用对应模块的方法')
    try:
        args=json.loads(options.args)
    except json.JSONDecodeError as exc:
        parser.error(str(exc))
    if not isinstance(args,list):parser.error('--args 必须为 JSON 数组')
    result=getattr(module.Solution(),names[0])(*args)
    # LeetCode 原地修改题通常返回 None，显示修改后的第一个参数。
    print(json.dumps(args[0] if result is None else result,ensure_ascii=False))


if __name__=='__main__':main()
