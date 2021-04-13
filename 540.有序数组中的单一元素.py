'''
Author: Zhou Hao
Date: 2021-04-13 21:23:35
LastEditors: Zhou Hao
LastEditTime: 2021-04-13 21:37:33
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
from typing import List


class Solution:
    
    '''hash'''
    # def singleNonDuplicate(self, nums: List[int]) -> int:
        # from collections import Counter

        # count = Counter(nums)
        # for k,v in count.items():
        #     if v == 1:return k


    '''stack'''
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     stack = []
        
    #     for n in nums:
    #         if not stack:stack.append(n)
    #         elif n == stack[-1]:stack.pop()
    #         elif n!= stack[-1]:stack.append(n)
        
    #     return stack[-1]


    '''二分'''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left,right = nums[0],nums[-1]

        while left <right:
            mid = (left + right) //2
            if nums.count(mid) ==1:return mid
            
            small_nums = 0
            for n in nums:
                if n<mid:small_nums += 1
            
            if small_nums %2 == 0:left = mid +1
            else:right = mid
            
        return left

    
            
        
# @lc code=end

