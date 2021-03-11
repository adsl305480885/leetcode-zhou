'''
Author: Zhou Hao
Date: 2021-03-11 16:27:21
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 17:08:10
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1072 lang=python3
#
# [1072] 按列翻转得到最大值等行数
#

# @lc code=start
class Solution:

        #查找每一行的       相同行和相反行的总数,
        #最大的那个就是答案
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        count = {}
        #字典记录每行的出现次数
        for i in matrix:
            i = tuple(i)
            count[i] = count.get(i,0) +1
        
        # print(count)
        res = 0

        #找每一行的   相同行和相反行的总数
        for k,v in count.items():
            reverse = tuple([1-x for x in k])
            temp = v        #当前相同行的数量
            
            if reverse in count: #如果存在相反行
                temp += count[reverse]      #相同行+ 相反行

            res = max(res,temp)
        return res
            



# @lc code=end

