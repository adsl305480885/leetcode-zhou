'''
Author: Zhou Hao
Date: 2021-02-22 23:54:24
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 00:04:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        # print(hashmap)
        # print(min(hashmap,key=hashmap.get))
        return min(hashmap,key=hashmap.get)

# @lc code=end

