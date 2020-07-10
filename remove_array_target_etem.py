# -*- coding: utf-8 -*-
# Created by EaApple on 7/10/2020
# Copyright (c) 2020 EaApple. All rights reserved. 元素的顺序可以改变  反向循环  只需要将
from typing import List


class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     flag = len(nums)  # 用于动态变化的数组
    #     for i in range(len(nums) - 1, -1, -1):  # 只需要查找前面的值
    #         if nums[i].__eq__(val):
    #             if i < flag - 1:  # 不是数组微末的值 就进行覆盖
    #                 for j in range(i, flag - 1, 1):
    #                     nums[j] = nums[j + 1]
    #             flag -= 1
    #     return len(nums[0:flag])

    def removeElement(self, nums: List[int], val: int) -> int:
        # 采用交换定律  反向
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)

    def removeElement1(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)

# nums: List[int] = [3, 2, 2, 3]
# nums: List[int] = [1, 2, 3, 5, 3]
nums: List[int] = [0, 1, 2, 2, 3, 0, 4, 2]
# nums: List[int] = [0, 1, 2, 2, 3, 0, 4, 2]
for i in range(Solution().removeElement(nums, 2)):
    print(nums[i])
