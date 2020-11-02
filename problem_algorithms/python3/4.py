from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = 0.0
        merge_list = []
        # 在两个数组最后设置结束标志，当数组遍历到此处时可以辨别出已经到达数组结尾
        nums1.append(1000001)
        nums2.append(1000001)
        # 遍历指针
        i = 0
        j = 0
        # 判定条件：当两个数组都遍历到结尾时停止遍历
        while(nums1[i] != 1000001 or nums2[j] != 1000001):
            # 依次遍历两个数组中的值，将较小的那个添加到合并数组中，并将较小值所在的数组指针加 1
            if nums1[i] <= nums2[j]:
                merge_list.append(nums1[i])
                i = i + 1
            else:
                merge_list.append(nums2[j])
                j = j + 1
        if len(merge_list) % 2 == 1:
            index = int((len(merge_list)-1)/2)
            result = merge_list[index]
        else:
            index = int(len(merge_list)/2)
            result = (merge_list[index] + merge_list[index-1])/2
        return result.__float__()


x = Solution()
print(x.findMedianSortedArrays([1, 2], [3, 4]))
