'''
Author: Zhou Hao
Date: 2021-03-17 20:23:53
LastEditors: Zhou Hao
LastEditTime: 2021-03-17 20:50:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=861 lang=python3
#
# [861] 翻转矩阵后的得分
#

# @lc code=start
class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        row = len(A)    #行
        colunm = len(A[0])  #列

        #贪心,最大的位数必须是1
        #1.把行首为0的进行行翻转，保证第一列全是1
        for i in range(row):
            if A[i][0] == 0:
                A[i] = [1-x for x in A[i]]

        #2.保证后面每列1的数量大于0
        for j in range(1,colunm): #列
            sum_temp = 0
            for i in range(row):  #行
                sum_temp += A[i][j]     #计算1的个数

            if sum_temp < row/2:        #1的个数少于一半，反转列
                for i in range(row):
                    A[i][j] = 1-A[i][j]

        res = 0 
        for a in A:
            a = [str(x) for x in a]
            temp = '0b'+ ''.join(a)
            # print(temp,int(temp,2))     #字符串转二进制
            res += int(temp,2)


        return res
# @lc code=end

