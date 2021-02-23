'''
Author: Zhou Hao
Date: 2021-02-23 11:40:03
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 11:53:38
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        border = 0
        for i in range(len(grid)):      #行
            for j in range(len(grid[0])):   #列
                if grid[i][j] == 1:
                    border += 4
                    if i>0 and grid[i-1][j] ==1 :#上
                        border -= 2
                        # print(i,j,'上')
                    if j>0 and grid[i][j-1] == 1:#左
                        border -= 2 
                        # print(i,j,'左')
        return border
# @lc code=end

