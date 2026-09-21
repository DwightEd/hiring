"""二叉树序列化
题意与思路：使用含空节点标记的 BFS 序列；反序列化按同一顺序构造。
复杂度：O(n) 时间和空间。
来源：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
"""

from collections import deque

class TreeNode:
    def __init__(self,val=0,left=None,right=None): self.val,self.left,self.right=val,left,right

class Codec:
    def serialize(self,root):
        queue,result=deque([root]),[]
        while queue:
            node=queue.popleft()
            if node is None: result.append('#')
            else:
                result.append(str(node.val))
                queue.extend((node.left,node.right))
        return ','.join(result)
    def deserialize(self,data):
        values=iter(data.split(','))
        first=next(values)
        if first=='#': return None
        root=TreeNode(int(first))
        queue=deque([root])
        while queue:
            node=queue.popleft()
            for side in ('left','right'):
                value=next(values)
                if value!='#':
                    child=TreeNode(int(value))
                    setattr(node,side,child)
                    queue.append(child)
        return root
