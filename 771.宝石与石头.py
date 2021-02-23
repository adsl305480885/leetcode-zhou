'''
Author: Zhou Hao
Date: 2021-02-23 15:00:50
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 20:48:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for s in stones:
            if s in jewels:
                res += 1
        return res
        
# @lc code=end

