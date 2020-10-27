from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(root):
            # nonlocal result
            if root == None:
                return
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return result
