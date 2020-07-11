# -*- coding: utf-8 -*-
# Created by EaApple on 7/11/2020
# Copyright (c) 2020 EaApple. All rights reserved.
from typing import List

class Solution(object):
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for i in range(1, len(prices), 1):
            if prices[i]>prices[i-1]:
                max_profit += prices[i]-prices[i-1]
        return max_profit

nums: List[int] = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(nums))
