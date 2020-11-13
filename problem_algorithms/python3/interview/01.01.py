class Solution:
    def isUnique(self, astr: str) -> bool:
        flag = True
        letter_dic = {}
        for letter in astr:
            if letter not in letter_dic:
                letter_dic[letter] = letter
            else:
                flag = False
        return flag