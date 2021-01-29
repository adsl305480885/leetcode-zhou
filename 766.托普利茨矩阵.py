'''
Author: Zhou Hao
Date: 2021-01-26 10:50:14
LastEditors: Zhou Hao
LastEditTime: 2021-01-28 16:45:58
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#

# @lc code=start
class Solution:
    '''方法一: 在满足 r1 - c1 == r2 - c2 的情况下，这两个点属于同一条对角线'''
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     row = len(matrix)   #行
    #     colunm = len(matrix[0]) #列
    #     line  = {}

    #     for r in range(row):
    #         for c in range(colunm):
    #             if r -c not in line:
    #                 print(r,c)
    #                 line[r-c] = matrix[r][c]    #存入每条对角线上的第一个值
    #             if matrix[r][c] != line[r-c]:   #判断对角线上的元素是否相等
    #                 return False
                    
    #     return True


    '''方法二:
        因为第一行和第一排都是对角线上的第一个元素，所以直接省略
        遍历的时候看是否等于左上角
    '''
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)   #行
        colunm = len(matrix[0]) #列

        for r in range(1,row):
            for c in range(1,colunm):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False

        return True



# @lc code=end

