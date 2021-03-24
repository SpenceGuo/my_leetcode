class Solution:
    # 穷举所有子序列
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        count = 0
        length = len(s)
        for i in range(length):
            for j in range(i, length):
                if self.judge(s[i:j+1]):
                    count += 1
        return count

    def judge(self, s: str) -> bool:
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True


"""
dp[i][j] 表示 s[i...j]是否为回文子串
初始化
if j-i==0: dp[i][j]=1
if j-i==1: dp[i][j] = s[i]==s[j]
迭代更新
if j-i>=2: dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
重点：根据递推公式, 右侧的横纵坐标之差更小, 所以遍历的时候可以按照 k=j-i 从小到大遍历
返回结果
回文子串数目 ans = dp 中等于1 的元素之和
"""
class Solution1:
    # 动态规划
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for k in range(n):
            # i+k<n => i<n-k
            for i in range(n - k):
                j = i + k
                if k == 0:
                    dp[i][j] = True
                elif k == 1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j]: count += 1
        return count


x = Solution1()
print(x.countSubstrings('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))



