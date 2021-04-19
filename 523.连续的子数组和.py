'''
Author: Zhou Hao
Date: 2021-04-19 16:35:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 20:03:01
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#

# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2: return False
        
        dp, cur = {0: -1}, 0
        for idx, num in enumerate(nums):
            cur += num
            cur %= k

            pre = dp.setdefault(cur, idx)
            if idx - pre > 1:       #通过索引判断长度
                return True
        return False
        
# @lc code=end

