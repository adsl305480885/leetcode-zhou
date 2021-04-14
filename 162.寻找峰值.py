'''
Author: Zhou Hao
Date: 2021-04-14 09:25:28
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 11:00:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
from typing import List


class Solution:

    # def findPeakElement(self, nums: List[int]) -> int:
    #     length = len(nums)
    #     if length == 1:return 0
    #     for i in range(1,length-1):
    #         if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
    #             return i
    #     if nums[-1] > nums[-2]:return length-1
    #     return 0 

    '''根据索引二分'''
    def findPeakElement(self, nums: List[int]) -> int:
        left ,right = 0,len(nums)-1
        while left <=right:
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left 

        
# @lc code=end

