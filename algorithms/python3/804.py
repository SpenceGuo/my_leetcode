from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        result = {}
        mol_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for s in words:
            str_mol = ""
            for i in range(0, s.__len__()):
                str_mol = str_mol + mol_code[ord(s[i])-97]
            result[str_mol] = str_mol
        return result.__len__()


x = Solution()
print(x.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
