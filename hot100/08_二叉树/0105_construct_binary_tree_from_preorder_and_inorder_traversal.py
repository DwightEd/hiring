"""105. 从前序与中序遍历序列构造二叉树
题意：根据互异节点值的前序和中序遍历重建二叉树。
思路：栈保存尚未完成中序访问的祖先；遇到中序当前值就连续回退。
时间：O(n)；空间：O(h)，不计输出。
原题：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack, index = [root], 0
        for i in range(1, len(preorder)):
            child = TreeNode(preorder[i])
            node = stack[-1]
            if node.val != inorder[index]:
                node.left = child
            else:
                while stack and stack[-1].val == inorder[index]:
                    node = stack.pop()
                    index += 1
                node.right = child
            stack.append(child)
        return root
