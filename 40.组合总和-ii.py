'''
Author: Zhou Hao
Date: 2021-04-22 13:35:58
LastEditors: Zhou Hao
LastEditTime: 2021-04-22 13:56:21
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    
    '''回溯，因为结果不要求顺序，所所以状态变量是start索引'''
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        
        def dfs(start,target):
            if target <0 :return
            if target == 0:
                if track not in res:
                    res.append(track[:])
                return

            for i in range(start,length):
                '''剪枝'''

                if candidates[i] > target:
                    continue
                
                #因为candidates 中的每个数字在每个组合中只能使用一次。
                #candidates已经排序，如果遇到重复元素，结果必然相同，所以直接跳过
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                


                track.append(candidates[i])
                dfs(i+1,target-candidates[i])
                track.pop()
            
        length = len(candidates)
        res,track = [],[]
        candidates.sort()       #有重复元素先排序
        dfs(0,target)
        return res

# @lc code=end

