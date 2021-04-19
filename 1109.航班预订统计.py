'''
Author: Zhou Hao
Date: 2021-04-19 20:11:57
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 20:31:34
Description: file content‘
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#

# @lc code=start
# from typing import List


class Solution:
    '''差分数组'''
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * n

        for book in bookings:
            i = book[0] - 1
            j = book[1] - 1
            diff[i] += book[2]
            if j+1 < n:
                diff[j+1] -= book[2]
                
        # print(diff)

        res = [0]* n
        res[0] = diff[0]

        for i in range(1,n,1):
            res[i] = res[i-1] + diff[i]

        # print(res)
                
        return res
# @lc code=end

