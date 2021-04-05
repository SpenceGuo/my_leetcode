class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, m+1):  # 列数
            for j in range(1, n+1):  # 行数
                if text1[i-1] == text2[j-1]:
                    dp[j][i] = dp[j-1][i-1] + 1  # 注意行和列的下标！！！
                else:
                    dp[j][i] = max(dp[j-1][i], dp[j][i-1])
        return dp[n][m]


x = Solution()
print(x.longestCommonSubsequence('abcde', 'ace'))
