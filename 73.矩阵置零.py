'''
Author: Zhou Hao
Date: 2021-04-20 21:42:10
LastEditors: Zhou Hao
LastEditTime: 2021-04-20 22:01:13
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       
        row_len = len(matrix)
        colunm_len = len(matrix[0])
        row = set()
        colunm = set()

        for i in  range(row_len):
            for j in range(colunm_len):
                if matrix[i][j] == 0:
                    row.add(i)
                    colunm.add(j)
        
        for i in  range(row_len):       #先改行，后改列
            if i in row:
                matrix[i] = [0]*colunm_len
                    
        for j in range(colunm_len):
            for i in range(row_len):
                if j in colunm:matrix[i][j] = 0

# @lc code=end

