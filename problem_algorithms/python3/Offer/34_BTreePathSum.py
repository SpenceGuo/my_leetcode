from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        result, path = [], []

        def recur(root: TreeNode, tar: int):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                """
                记录路径时若直接执行 res.append(path) ，则是将 path 列表对象 加入了 res ；
                后续 path 对象改变时， res 中的 path 对象 也会随之改变（因此肯定是不对的，
                本来存的是正确的路径 path ，后面又 append 又 pop 的，就破坏了这个正确路径）。
                list(path) 相当于新建并复制了一个 path 列表，因此不会受到 path 变化的影响。
                """
                result.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, target)
        return result


class Solution:
    def hasPathSum(self , root , sum ):
        result, temp = [], []
        def recur(root: TreeNode(), target: int):
            if not root: return
            temp.append(root.val)
            target -= root.val
            if target == 0 and not root.left and not root.right:
                result.append(list(temp))
            recur(root.left, target)
            recur(root.right, target)
            temp.pop()
        recur(root, sum)
        return result