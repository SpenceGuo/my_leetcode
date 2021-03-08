from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                p = queue.pop(0)
                temp.append(p.val)
                if p.left: queue.append(p.left)
                if p.right: queue.append(p.right)
            result.append(temp)
        return result
