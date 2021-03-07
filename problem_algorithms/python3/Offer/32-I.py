from typing import List
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉树的层次遍历（借助队列实现）
# 过程：
# 先将根节点进队，在队列不为空时循环：
# 1.从队列中出列一个节点并访问它
# 2.若它有左孩子节点，将左孩子节点入队
# 3.若它有右孩子节点，将右孩子节点入队
# 如此操作直到队列为空为止
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result, queue = [], []
        # 将根节点进队
        queue.append(root)
        # 在队列不为空时循环
        while queue:
            p = queue.pop(0)
            result.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return result
