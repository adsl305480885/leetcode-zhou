'''
Author: Zhou Hao
Date: 2021-02-24 23:02:48
LastEditors: Zhou Hao
LastEditTime: 2021-02-24 23:14:21
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1512 lang=python3
#
# [1512] 好数对的数目
#

# @lc code=start
class Solution:
    #数学推导，组合
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def jiecheng(n):
            totla = 1
            for i in range(1,n+1,):
                totla *= i
            return totla

        from collections import Counter
        counter = Counter(nums).values()
        res = 0
        for c in counter:
            if c != 1:
                res += jiecheng(c)//(jiecheng(c-2)*2)

        return res

# @lc code=end

