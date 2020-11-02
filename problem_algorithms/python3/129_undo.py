# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = 0
        result_list = []
        def dfs(root):
            if not root:
                return
            result_list.append(root.val)
            dfs(root.left)
            dfs(root.right)

        return result

