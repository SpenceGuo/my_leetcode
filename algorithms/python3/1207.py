from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        result = True
        count_list = []
        arr_dist = []
        for i in range(0, len(arr)):
            if arr[i] not in arr_dist:
                arr_dist.append(arr[i])
                count_list.append(arr.count(arr[i]))
            else:
                pass
        for j in range(0, len(count_list)-1):
            for k in range(j+1, len(count_list)):
                if count_list[j] == count_list[k]:
                    result = False
                else:
                    pass
        return result


x = Solution()
result = x.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
print(result)
