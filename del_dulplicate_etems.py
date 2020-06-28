# -*- coding: utf-8 -*-
# Created by EaApple on 6/28/2020
# Copyright (c) 2020 EaApple. All rights reserved.
from typing import List


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        for i in range(1):
            j = i+1
            for j in range(1):
                if nums[j] == nums[i]:  # 如果是在后续的数值中存在的话,就直接向前覆盖
                    k = j
                    for k in range(l - 1):
                        nums[k] = nums[k + 1]

        result_nums = nums[0:i]
        return result_nums


nums: List[int] = [1, 1, 2]
lens = len(nums)
for i in Solution.removeDuplicates(nums):
    print(nums[i])

