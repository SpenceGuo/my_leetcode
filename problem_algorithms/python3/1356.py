from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        for j in range(1, len(arr)):
            # a[j] 代表当前需要插入有序序列的数，a[0...i]为前i+1个已经排序号的有序序列
            key = arr[j]
            i = j - 1
            # 将a[j]与前j个有序数依次比较大小，并找到合适的位置插入
            while i >= 0 and str(bin(arr[i])).count("1") > str(bin(key)).count("1"):
                arr[i + 1] = arr[i]
                i = i - 1
                arr[i + 1] = key
            else:
                pass
        return arr

