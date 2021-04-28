'''
Author: Zhou Hao
Date: 2021-04-22 10:26:45
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 23:22:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    '''回溯，状态变量是start,答案不看顺序'''
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start):
            if len(track) >= k:
                res.append(track[:])
                return 

            for i in range(start,n+1):
                track.append(i)
                dfs(i+1)
                track.pop()
            
        res,track  = [],[]
        dfs(1)
        return res 
# @lc code=end

