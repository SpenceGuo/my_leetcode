from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root: return result
        flag = 0
        queue = [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                p = queue.pop(0)
                temp.append(p.val)
                if p.left: queue.append(p.left)
                if p.right: queue.append(p.right)
            flag += 1
            if flag % 2 == 0:
                temp.reverse()
                result.append(temp)
            else:
                result.append(temp)
        return result

