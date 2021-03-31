'''
Author: Zhou Hao
Date: 2021-03-31 13:24:54
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 13:57:59
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=539 lang=python3
#
# [539] 最小时间差
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(set(timePoints)) < len(timePoints):  #check the repeat
            return 0

        #turn time to minutes
        times = [int(t[:2])*60+int(t[3:]) for t in timePoints]
        times = sorted(times)       #ascending
        res = float("inf")  #infinity + 
        i = 0

        while i < len(times)-1: #attention to the board
            if times[i+1] - times[i] > 720:
                res = min(res,1440-times[i+1]+times[i])
            else:
                res = min(res,times[i+1]-times[i])
                
            i+=1
            
        if times[-1] - times[0] > 720:  #compare the biggest and the smallest
            res = min(res,1440-times[-1]+times[0])

        return res
# @lc code=end

