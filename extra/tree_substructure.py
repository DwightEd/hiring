"""二叉树子结构
题意与思路：非空 B 是否能匹配 A 的某个节点起始的部分结构；B 为空按题型约定返回 False。
复杂度：最坏 O(mn) 时间，O(m+n) 辅助空间。
来源：公开面经题型；见 companies/README.md 的逐题映射。
"""

def is_substructure(a,b):
    if a is None or b is None: return False
    def matches(root,pattern):
        stack=[(root,pattern)]
        while stack:
            node,wanted=stack.pop()
            if wanted is None: continue
            if node is None or node.val!=wanted.val: return False
            stack.extend(((node.left,wanted.left),(node.right,wanted.right)))
        return True
    stack=[a]
    while stack:
        node=stack.pop()
        if matches(node,b): return True
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    return False
