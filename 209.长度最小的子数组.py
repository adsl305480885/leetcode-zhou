'''
Author: Zhou Hao
Date: 2021-04-14 11:04:49
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 12:07:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
from typing import List


class Solution:
    
    '''滑动窗口O(n)'''
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    #     if sum(nums) < target:return 0
    #     left,right = 0,0
    #     length = float('inf')
    #     window_sum = 0

    #     #先滑右，满足条件后再滑左，直到不满足条件就继续滑右
    #     for right in range(len(nums)):
    #         window_sum += nums[right]
    #         while window_sum>=target:       #满足条件
    #             length = min(length,right-left+1)
    #             window_sum -= nums[left]
    #             left +=1        #滑左
                
    #     return length

    '''前缀和+二分'''
    #TODO
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:




# @lc code=end

