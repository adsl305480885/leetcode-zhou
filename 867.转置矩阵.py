'''
Author: Zhou Hao
Date: 2021-01-24 15:06:47
LastEditors: Zhou Hao
LastEditTime: 2021-01-24 16:55:37
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    '''交换角标'''
    # def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # row = len(A)    #原矩阵的行
        # cloumn = len(A[0])       #原矩阵的列

        # res = []
        # for c in range(cloumn):     #每行
        #     rows_list = []      #每行的空列表
        #     for r in range(row):    #每列
        #         rows_list.append(A[r][c])
        #         print(A[r][c])
        #     res.append(rows_list)

        # print(res)
        # return res
        

    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)    #原矩阵的行
        cloumn = len(A[0])       #原矩阵的列

        res = [[0 for r in range(row)] for c in range(cloumn)]
        for c in range(cloumn):     #每行
            for r in range(row):    #每列
                print(A[r][c])
                res[c][r] = A[r][c]
                
        return  res

        
        
# @lc code=end

