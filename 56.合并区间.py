'''
Author: Zhou Hao
Date: 2021-03-16 13:21:29
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 15:51:58
Description: file content#
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    #贪心
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:return intervals

        #lamda匿名函数，冒号左边是参数，冒号右边是返回值。 变量命名空间只存在lamda里面
        intervals = sorted(intervals,key= lambda x:x[0])    #按区间第一个升序
        
        res = []
        res.append(intervals[0])

        #贪心遍历,选最大的
        for i in intervals:
            if i[0] > res[-1][-1]:     #没重叠
                res.append(i)
            else:
                if i[1] > res[-1][-1]:  #重叠,取并集
                    res[-1][-1] = i[1]
        
        # print(res)
        return res

# @lc code=end

