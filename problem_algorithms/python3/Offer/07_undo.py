from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def recursion(root, left, right):
            if left > right:
                return
            node = TreeNode(preorder[root])
            i = dic[preorder[root]]
            node.left = recursion(root+1, left, i-1)
            node.right = recursion(i-left+root+1, i+1, right)
            return node

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recursion(0, 0, len(inorder-1))
