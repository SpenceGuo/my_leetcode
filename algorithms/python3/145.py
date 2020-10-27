from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            dfs(root.right)
            result.append(root.val)

        dfs(root)
        return result
