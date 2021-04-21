'''
Author: Zhou Hao
Date: 2021-04-20 22:03:10
LastEditors: Zhou Hao
LastEditTime: 2021-04-20 22:14:30
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:

    # def rotate(self, nums: List[int], k: int) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     length = len(nums)
    #     if k%length == 0:return nums
    #     k = k %length
    #     nums[:] = nums[length-k:]+nums[:length-k]

        
    '''三次翻转，先整体翻转，然后根据K的位置前后局部翻转'''
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


        
# @lc code=end

