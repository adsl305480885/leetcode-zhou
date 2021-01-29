'''
Author: Zhou Hao
Date: 2021-01-26 10:23:12
LastEditors: Zhou Hao
LastEditTime: 2021-01-26 10:38:53
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution:
    '''
    方法一：先排序升序，然后选索引为0,2,4,6的元素相加
    '''
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum_ = 0
        for i in  range(0,len(nums),2):
            sum_ += nums[i]
        return sum_
        

    
# @lc code=end

