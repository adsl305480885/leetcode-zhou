'''
Author: Zhou Hao
Date: 2021-04-26 16:57:44
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 17:13:02
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    # def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    #     nums = [i for i in range(1,10)]
    #     def dfs(start,target):
    #         if target == 0 and len(track)==k:
    #             res.append(track[:])
    #             return

    #         for i in range(start,9):
    #             if nums[i] > target:continue    #剪枝

    #             track.append(nums[i])
    #             dfs(i+1,target-nums[i])
    #             track.pop()     #回溯

        
    #     res,track = [],[]
    #     dfs(0,n)
    #     return res



    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start,target):
            if target == 0 and len(track)==k:
                res.append(track[:])
                return

            for i in range(start,10):
                if i > target:continue    #剪枝

                track.append(i)
                dfs(i+1,target-i)
                track.pop()     #回溯
 
        res,track = [],[]
        dfs(1,n)
        return res
        
# @lc code=end

