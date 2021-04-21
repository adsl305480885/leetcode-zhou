'''
Author: Zhou Hao
Date: 2021-04-21 11:04:23
LastEditors: Zhou Hao
LastEditTime: 2021-04-21 16:02:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    '''回溯就是DFS ，二叉树的前序遍历'''
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums,track):
            if len(nums) == len(track):
                res.append(track[:])        #TODO注意拷贝一份新数组
                return 

            for i in range(len(nums)):
                if nums[i] in  track:   #剪树
                    continue

                track.append(nums[i])
                dfs(nums,track)
                track.pop()

        
        res = []
        track = []
        dfs(nums,track)
        return res
# @lc code=end

