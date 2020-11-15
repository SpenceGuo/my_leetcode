from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for i in range(0, len(points)-1):
            x = abs(points[i][0]-points[i+1][0])
            y = abs(points[i][1]-points[i+1][1])
            count += min(x, y)
            count += abs(x-y)
        return count