'''
Author: Zhou Hao
Date: 2021-01-28 22:04:49
LastEditors: Zhou Hao
LastEditTime: 2021-01-29 20:58:39
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#

# @lc code=start
class Solution:
    
    #天平思想，遍历的时候移动计算左右两边的重量
    def pivotIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_i = 0
        
        if sum(nums[1:]) == 0:
                return 0
        # if sum(nums[:-1]) == 0:
        #     return len(nums)-1

        for i in range(len(nums)-1):
            sum_i += nums[i]
            if sum_i == sum_nums - nums[i+1] - sum_i:
                return i+1
                
        return -1
# @lc code=end

