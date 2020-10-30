# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1

p = TreeNode(3)
p.left = TreeNode(9)
p.left.left = TreeNode(9)
p.left.right = TreeNode(9)
p.right = TreeNode(20)
x = Solution()
print(x.maxDepth(p))
