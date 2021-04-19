'''
Author: Zhou Hao
Date: 2021-04-19 22:28:52
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 22:43:05
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:

    '''滑动窗口'''
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        length = len(customers)

        peoples = 0
        for i in range(length):     #统计原来不生气的人数
            if grumpy[i] == 0:peoples += customers[i]

        # print(peoples)


        #统计大小为X的滑动窗口内，赶走最多的人数
        max_people = 0
        res = 0
        for i in range(length):
            if i < X:       #初始窗口赶走的人数
                if grumpy[i] == 1:
                    max_people += customers[i]
                if i == X-1:
                    res = max_people

            else:
                if grumpy[i] == 1:
                    max_people += customers[i]
                if grumpy[i-X] == 1:
                    max_people -= customers[i-X]
                
                res = max(res,max_people)
        # print(res)

        return res + peoples
# @lc code=end

