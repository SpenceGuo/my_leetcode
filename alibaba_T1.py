import sys
from typing import List


def getMissK(k: int, nums: List):
    index = 0
    i = nums[0]
    while index < len(nums):
        index += 1
        i += 1
        if index < len(nums) and nums[index] > i:
            if k <= (nums[index]-i):
                return i + k - 1
            k = k-(nums[index]-i)
            i = nums[index]
    else:
        return nums[-1]+k


# print(getMissK(5,[4,7,9,10]))
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    k_list, nums_list = [], []
    result = []
    for i in range(2*n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        line_list = list(map(int, line.split()))
        if i % 2 == 0: k_list.append(line_list[1])
        if i % 2 == 1: nums_list.append(line_list)
    for j in range(len(k_list)):
        result.append(getMissK(k_list[j], nums_list[j]))
    for a in range(len(result)):
        print(result[a])
