'''
Author: Zhou Hao
Date: 2021-04-22 13:10:51
LastEditors: Zhou Hao
LastEditTime: 2021-04-22 13:35:39
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    '''
    什么时候使用 used 数组，什么时候使用 begin 变量
    有些朋友可能会疑惑什么时候使用 used 数组，什么时候使用 begin 变量。这里为大家简单总结一下：

    排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），
        需要记录哪些数字已经使用过，此时用 used 数组；
    组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），
        需要按照某种顺序搜索，此时使用 begin 变量。
    
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start,target):
            if target < 0:return
            if target == 0:
                res.append(track[:])
                return

            for i in range(start,len(candidates)):
                track.append(candidates[i])
                dfs(i,target-candidates[i])     #因为能重复使用，所以从i开始递归
                track.pop()
            

        res,track = [],[]
        dfs(0,target)
        return res
        

# @lc code=end

