'''
Author: Zhou Hao
Date: 2021-04-19 15:44:43
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 15:59:48
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#

# @lc code=start
class Solution:

    '''哈希前缀和'''
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #偶数变0，奇数变1，题目转换为求和为k的字数组
        nums = [1 if n%2 !=0 else 0 for n in nums ]

        presum = {0:1}
        res = 0
        sum_i = 0
        length = len(nums)

        for i in range(length):
            sum_i += nums[i]
            sum_j = sum_i - k
            if sum_j in presum:
                res += presum[sum_j]
            presum[sum_i] = presum.get(sum_i,0)+1

        return res
        
# @lc code=end

