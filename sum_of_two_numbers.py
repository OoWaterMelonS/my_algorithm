# -*- coding: utf-8 -*-
# Created by EaApple on 6/27/2020
# Copyright (c) 2020 EaApple. All rights reserved.
def twoSum(nums, target):
    lens = len(nums)
    j = -1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if (nums.count(target - nums[i]) == 1) & (
                    target - nums[i] == nums[i]):  # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
                continue
            else:
                j = nums.index(target - nums[i], i + 1)  # index(x,i+1)是从num1后的序列后找num2
                break
    if j > 0:
        return [i, j]
    else:
        return []


def sum_two(nums, target):
    lens = len(nums)
    j = -1
    for i in range(lens):
        if (target - nums[i]) in nums:
            if nums.count(target - nums[i]) == 1 & target - nums[i] == nums[i]:
                continue
            else:
                j = nums.index(target - nums[i], i + 1)
                break
        if j > 0:
            return [i, j]
        else:
            return []
