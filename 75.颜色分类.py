'''
Author: Zhou Hao
Date: 2021-04-14 17:18:45
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 19:00:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
from typing import List


class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     nums.sort()
        

    '''三指针'''
    def sortColors(self, nums: List[int]) -> None:
        left ,right = 0,len(nums)-1
        i = 0
        while i<= right:        #注意循环条件
            if nums[i] == 0:
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
                i+=1
            elif nums[i] == 2:
                nums[i],nums[right] = nums[right],nums[i]   #跟后面交换后，i不用递增
                right-=1
            else:i+=1
            
        print(nums)
# @lc code=end

