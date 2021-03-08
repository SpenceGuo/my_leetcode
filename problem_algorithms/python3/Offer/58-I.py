class Solution:
    def reverseWords(self, s: str) -> str:
        temp = [x for x in s.split(' ') if x != '']
        temp.reverse()
        return ' '.join(temp)
