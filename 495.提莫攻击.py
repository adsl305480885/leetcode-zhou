'''
Author: Zhou Hao
Date: 2021-04-20 22:27:13
LastEditors: Zhou Hao
LastEditTime: 2021-04-21 11:03:50
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=495 lang=python3
#
# [495] 提莫攻击
#

# @lc code=start
class Solution:

    '''set超时'''
    # def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    #     time_set = set()
    #     for time in timeSeries:
    #         for i in range(duration):
    #             if time+i not in time_set:
    #                 time_set.add(time+i)

    #     return len(time_set)


    '''推数学公式'''
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        length = len(timeSeries)
        if length ==0:return 0
        if length == 1 :return duration

        res = duration
        for i in range(1,len(timeSeries),1):
            if timeSeries[i] - timeSeries[i-1] <duration:
                res = res + (timeSeries[i] - timeSeries[i-1])
            else:
                res += duration
        
        return res
# @lc code=end

