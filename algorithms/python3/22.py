"""
数字 n代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
"""
class Solution:
    def generateParenthesis(self, n):
        left = []
        right = []
        for i in range(0, n):
            left.append("(")
            right.append(")")
