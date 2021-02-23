'''
Author: Zhou Hao
Date: 2021-02-23 20:56:03
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 21:07:53
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1365 lang=python3
#
# [1365] 有多少小于当前数字的数字
#

# @lc code=start
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nn = sorted(nums)
        hashmap = {}
        
        for i,n in enumerate(nn):
            if n not in hashmap:
                hashmap[n] = i

        print(hashmap)
        
        res = []
        for n in nums:
            res.append(hashmap[n])
        return res


# @lc code=end

