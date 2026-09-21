import importlib.util
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def catalog(name):
    return json.loads((ROOT / 'catalog' / (name + '.json')).read_text())


@lru_cache(None)
def module(group, identifier):
    row = next(row for row in catalog(group) if row['id'] == identifier)
    spec = importlib.util.spec_from_file_location(f'{group}_{identifier}', ROOT / row['path'])
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def solution(group, identifier):
    return module(group, identifier).Solution()


class Node:
    def __init__(self, val=0, next=None, left=None, right=None):
        self.val, self.next, self.left, self.right = val, next, left, right
        self.random = None


def linked(values):
    head = None
    for value in reversed(values):
        head = Node(value, next=head)
    return head


def values(head):
    result, seen = [], set()
    while head:
        if id(head) in seen:
            raise AssertionError('输出链表意外成环')
        seen.add(id(head))
        result.append(head.val)
        head = head.next
    return result


def tree(levels):
    if not levels or levels[0] is None:
        return None
    nodes = [Node(value) if value is not None else None for value in levels]
    children = iter(nodes[1:])
    for node in nodes:
        if node:
            node.left = next(children, None)
            node.right = next(children, None)
    return nodes[0]


def inorder(root):
    stack, output = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        output.append(root.val)
        root = root.right
    return output
