from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        result = paths[0][0]
        start = []
        end = []
        for j in range(0, len(paths)):
            start.append(paths[j][0])
            end.append(paths[j][1])
        start_end_dic = dict(zip(start, end))
        while result in start_end_dic:
            result = start_end_dic[result]
        return result


x = Solution()
paths = [["qMTSlfgZlC","ePvzZaqLXj"],["xKhZXfuBeC","TtnllZpKKg"],["ePvzZaqLXj","sxrvXFcqgG"],["sxrvXFcqgG","xKhZXfuBeC"],["TtnllZpKKg","OAxMijOZgW"]]
print(x.destCity(paths))
