'''
Author: Zhou Hao
Date: 2021-04-26 10:08:22
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 11:11:23
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def isValid(row,col,char):
            for i in range(9):
                if board[row][i] == char:return False
                if board[i][col] == char:return False
                if board[(row//3)*3+i//3][(col//3)*3+i%3] == char:return False
            return True

        def dfs(row,col):
            if col ==9: #剪枝,如果列数是9 继续下一行
                return  dfs(row+1,0)
                
            if row ==9 :        #行数达到9说明找到了一个可行解返回,终止条件
                return True
                
            if board[row][col] != '.':      #剪枝,非空位置不管
                return dfs(row,col+1)
            
            for  char in range(1,10):
                char = str(char)
                if not isValid(row,col,char):
                    continue

                board[row][col] = char
                if dfs(row,col+1):
                    return True
                board[row][col] = '.'       #回溯
            return False
            
        dfs(0,0)

        
# @lc code=end

