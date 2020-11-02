from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums2_dic = dict(zip(nums2, nums2))
        for i in range(0, len(nums1)):
            if nums1[i] in nums2_dic and nums1[i] not in result:
                result.append(nums1[i])
        return result