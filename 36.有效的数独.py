'''
Author: Zhou Hao
Date: 2021-02-26 23:51:32
LastEditors: Zhou Hao
LastEditTime: 2021-02-27 12:04:07
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashmap = {}
        row = len(board)    #行
        column = len(board[0])  #列

        #每行
        for i in board:
            for j in i:
                if (j not in hashmap) and j.isdigit():
                    hashmap[j] = 1
                elif not j.isdigit():
                    pass
                else:
                    # print('aaa\n',hashmap)
                    return False
            hashmap.clear()

        #每列
        hashmap.clear()
        for c  in range(column):
            for r in range(row):
                if board[r][c] not in hashmap and board[r][c].isdigit() :
                    hashmap[board[r][c]] = 1
                elif not board[r][c].isdigit():
                    pass
                else:
                    # print('bbb\n',hashmap)
                    return False
            hashmap.clear()


        #每格子
        hashmap.clear()
        c=r=0
        while c <9 and r<9:
            
            for c in range(c,c+3,1):
                for r in range(r,r+3,1):
                    # print(board[r][c],r,c)
                    if board[r][c] not in hashmap and board[r][c].isdigit():
                        hashmap[board[r][c]] = 1
                    elif not board[r][c].isdigit():
                        pass
                    else:
                        # print('ccc\n',hashmap)
                        return False
                r -=2


            if r+2 ==8 and c==8:
                break
            elif r+2 ==8 and c!=8:
                r = 0
                c+=1
            else:
                c -=2
                r +=3
            print(hashmap,r,c)
            hashmap.clear()
        return True
# @lc code=end

