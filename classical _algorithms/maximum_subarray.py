"""
problem of finding maximum sub-array
寻找某个数组的最大子数组问题
"""
from typing import List
import math


def find_cross_maximum_subarray(arr: List, low: int, mid: int, high: int):
    mid = math.floor(len(arr)/2)
    max_left = mid
    max_right = mid
    left_sum = -float("inf")
    right_sum = -float("inf")

    sum = 0
    for i in range(mid, low-1, -1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for j in range(mid + 1, high+1):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(arr: list, low: int, high: int):
    # 默认数组不为空
    if low == high:
        return 0, 0, arr[0]
    mid = math.floor((low + high)/2)
    left_low, left_high, left_sum = find_maximum_subarray(arr, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(arr, mid+1, high)
    cross_low, cross_high, cross_sum = find_cross_maximum_subarray(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    elif cross_sum >= left_sum and cross_sum >= right_sum:
        return cross_low, cross_high, cross_sum


print(find_cross_maximum_subarray([-3,2,-1,6,-1,3,5],0,3,6))
print(find_maximum_subarray([-3,2,-1,6,-1,3,5],0,6))
