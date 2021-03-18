'''
Author: Zhou Hao
Date: 2021-03-18 16:22:12
LastEditors: Zhou Hao
LastEditTime: 2021-03-18 16:39:32
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] 两地调度
#

# @lc code=start
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: (x[0]-x[1]))


        res = 0
        length = len(costs)
        for i in range(len(costs)):
            if i >= length//2: #去B
                res += costs[i][1]
            else:
                res += costs[i][0]
        return res
# @lc code=end

