'''
Author: Zhou Hao
Date: 2021-04-26 22:54:03
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 23:07:39
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#

# @lc code=start
class Solution:

    '''begin状态变量+uesd数组，有重复还有顺序'''
    def numTilePossibilities(self, tiles: str) -> int:
        
        def dfs(n):
            if n==m:
                return

            for i in range(m):
                if visit[i] and not (i>0 and sorted_tiles[i-1]==sorted_tiles[i] and visit[i-1]):                    
                    visit[i]=False
                    self.ans+=1
                    dfs(n+1)
                    visit[i]=True
        
        self.ans=0
        sorted_tiles=sorted(tiles)      #有重复先排序
        m=len(sorted_tiles)    #字符串长度
        visit=[True]*m  #允许访问
        dfs(0)
        return self.ans
        
# @lc code=end

