'''
Author: Zhou Hao
Date: 2021-01-20 22:17:00
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 22:31:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    '''方法一:'''
    # def missingNumber(self, nums: List[int]) -> int:
    #     for i in range(len(nums)+1):
    #         if i not in nums:
    #             return i
        
        
    '''方法二:'''
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = (1 + len(nums))*(len(nums)/2) 
        return int(sum_nums - sum(nums))
        
# @lc code=end

