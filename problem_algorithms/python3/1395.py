from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # 枚举三元组,时间复杂度 O(n^3)
        n = len(rating)
        count = 0
        for i in range(0, n-2):
            for j in range(i, n-1):
                for k in range(j, n):
                    if (rating[i]<rating[j] and rating[j]<rating[k]) or \
                            (rating[i]>rating[j] and rating[j]>rating[k]):
                        count += 1
        return count


class Solution1():
    def numTeams(self, rating: List[int]) -> int:
        # 枚举三元组的中间值,时间复杂度 O(n^2)
        count = 0
        n = len(rating)
        for i in range(1, n-1):
            xless = len([a for a in rating[:i] if a < rating[i]])
            xmore = len([b for b in rating[i+1:] if b > rating[i]])
            ymore = len([c for c in rating[:i] if c > rating[i]])
            yless = len([d for d in rating[i+1:] if d < rating[i]])
            count = count + xless*xmore + ymore*yless
        return count


x = Solution1()
print(x.numTeams([1, 2, 3, 4, 5, 6, 7]))
