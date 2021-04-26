'''
Author: Zhou Hao
Date: 2021-04-26 22:04:19
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 22:43:27
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start
class Solution:
    # def countArrangement(self, n: int) -> int:
    #     self.res = 0
        
    #     def dfs():
    #         if len(track) == n:
    #             self.res+=1
    #             return

    #         for i in range(1,n+1):
    #             if i in track:continue      #剪枝
    #             index = len(track) +  1
    #             if index % i !=0 and i% index !=0:
    #                 continue

    #             track.append(i)
    #             dfs()
    #             track.pop()

    #     track = []
    #     dfs()
    #     return self.res



    def countArrangement(self, n: int) -> int:
        global res,track,total
        res,track = 0,0
        total = sum(range(n+1))

        def dfs(index):
            global res,track,total

            if track == total:
                res += 1
                return

            for i in range(1,n+1):
                if used[i-1] == True:continue
                if index % i !=0 and i% index !=0:
                    continue
                
                track+=i
                used[i-1] = True
                dfs(index+1)
                track-=i
                used[i-1] = False


        used = [False] * n
        dfs(1)
        return res
# @lc code=end

