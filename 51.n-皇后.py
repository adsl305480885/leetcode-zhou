'''
Author: Zhou Hao
Date: 2021-04-22 13:57:07
LastEditors: Zhou Hao
LastEditTime: 2021-04-22 14:56:43
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.'* n ] * n      #初始化空棋盘
        
        def isValid(board,row,col):
            '''判断当前位置能不能放置皇后'''
            #因为皇后是从上往下放的，所以不用检查下面的位置,不用检查当前行

            #判断当前列上面是否冲突
            for i in range(row):
                if board[i][col] == 'Q':
                    return True
            # 右上
            for i,j in zip(range(row-1, -1, -1), range(col+1, n)):
                if(board[i][j] == 'Q'):
                    return True
            # 左上
            for i,j in zip(range(row-1,-1,-1), range(col-1, -1, -1)):
                if(board[i][j] == 'Q'):
                    return True

            return False


        def dfs(board,row):
            if row == n:
                res.append(board[:])
                return 

            for col in range(n):
                #剪枝，如果位置冲突，就跳过
                if isValid(board,row,col):
                    continue
                
                board[row] = '.'*col + 'Q' + '.'* (n-1-col)
                dfs(board,row+1)
                board[row] = '.'*n


        res = []
        dfs(board,0)
        return res
# @lc code=end

