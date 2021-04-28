'''
Author: Zhou Hao
Date: 2021-04-21 14:57:58
LastEditors: Zhou Hao
LastEditTime: 2021-04-22 10:10:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 1: return  [nums]


        def dfs(nums,track,used):
            if length == len(track):
                res.append(track[:])    #深拷贝
                return 

            for i in range(len(nums)):
                '''根据状态变量剪枝'''
                #剪枝条件1：用过的元素不能再使用
                #剪枝条件2：当当前元素和前一个元素值相同（此处隐含这个元素的 index>0 ），
                #           并且前一个元素还没有被使用过的时候，我们要剪枝
                if used[i] == True:
                    continue
                if i >0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue
                
                track.append(nums[i])
                used[i] = True
                
                dfs(nums,track,used)

                track.pop()
                used[i] = False


        used = [False] * length     #判断每个元素是否已经使用
        nums.sort()     #考虑重复元素一定要排序,搭配used状态变量
        res = []
        track = []
        dfs(nums,track,used)
        return res
# @lc code=end

