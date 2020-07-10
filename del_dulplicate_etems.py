# -*- coding: utf-8 -*-
# Created by EaApple on 6/28/2020
# Copyright (c) 2020 EaApple. All rights reserved.   去除掉数组中的重复值
from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int: #默认为了递增的情况,逆向删除
        for num_index in range(len(nums) - 1, 0, -1):
            if nums[num_index] == nums[num_index - 1]:
                nums.pop(num_index)
        return len(nums)

    # def removeDuplicates(self, nums: List[int]) -> int:  # 正向删除,乱序的情况也可以支持
    #     flag = len(nums)  # 用于存储实时变化的数组的长度,从开始向后遍历,同时数组长度在实时变化
    #     i = 0
    #     while i < flag:
    #         j = i + 1
    #         while j < flag:
    #             if nums[j] == nums[i]:
    #                 if j == flag - 1:  # 数组最后一个值和i位置上的值一样的情况  就直接flag减一 退出循环
    #                     flag -= 1
    #                 else:
    #                     k = j
    #                     while k < flag - 1:  # 依次向前覆盖,同时数组待循环长度减一
    #                         nums[k] = nums[k + 1]
    #                         k += 1
    #                     flag -= 1  # 数组有效长度减一
    #                     continue  # 因为原本j位置上的值被覆盖掉了,所以不必j+1
    #             j += 1
    #         i += 1
    #     return len(nums[0:flag])


nums: List[int] = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums: List[int] = [0, 1, 1, 2]
for i in range(Solution().removeDuplicates(nums)):
    print(nums[i])
