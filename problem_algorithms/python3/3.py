class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        解法思路：滑动窗口思路
        :param s:
        :return:
        """
        # 考虑极端值，即字符串 s 长度为 0 或 1 时的情况
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        best = 0
        temp_list = [s[0]]
        i, j = 0, 1
        while(j < len(s)):
            if s[j] not in temp_list:
                temp_list.append(s[j])
                j = j + 1
            else:
                i = i + 1
                temp_list.pop(0)
            if best < (j-i+1):
                best = j - i
        return best


x = Solution()
print(x.lengthOfLongestSubstring(" "))
