# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        merge = TreeNode(t1.val + t2.val)
        merge.left = self.mergeTrees(t1.left, t2.left)
        merge.right = self.mergeTrees(t1.right, t2.right)
        return merge
