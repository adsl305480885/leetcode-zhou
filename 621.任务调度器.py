'''
Author: Zhou Hao
Date: 2021-03-16 13:36:52
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 14:13:22
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
class Solution:
    #贪心
    #先找出次数最多的任务X，出现4次,n为2
    #画矩阵图
    # [
    #   x,0,0,
    #   x,0,0,
    #   x,0,0,
    #   x        #最后一行查看和X次数相同的任务有多少个
    # ]
    #   (4-1) * (2+1)   行*列  =  9
    #   9 + 最后一行 = 最短时间
    #如果算出来的时间小于任务次数就返回任务次数

    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        count = Counter(tasks)  #计算每个任务出现多少次
        times = list(count.values())
        x = max(times)     #次数最多
        last = times.count(x)  #最后一行
        res = (x-1) * (n+1) + last

        return max(res,sum(times))
        

        
# @lc code=end

