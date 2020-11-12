from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        # 注意：此 children 为 list 变量！
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def dfs(root):
            if not root:
                return
            children = root.children
            for child in children:
                dfs(child)
            result.append(root.val)

        dfs(root)

        return result
