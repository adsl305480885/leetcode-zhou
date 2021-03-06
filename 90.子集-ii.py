'''
Author: Zhou Hao
Date: 2021-04-21 16:04:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-22 10:10:51
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    '''参考47.全排列2'''
    

    '''迭代，去重'''
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     nums.sort()     #有重复元素一定要排序
    #     for i in nums:
    #         res = res + [[i] + num for num in res]

    #     index = 0
    #     while index < len(res):
    #         if res.count(res[index]) > 1:
    #             res.remove(res[index])
    #         else:index+=1

    #     return res



    '''回溯dfs'''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(start):
            res.append(track[:])

            for i in range(start,len(nums)):
                '''根据状态变量剪枝'''
                if i >start and nums[i] == nums[i-1]:       #剪枝
                    continue

                track.append(nums[i])
                dfs(i+1)
                track.pop()
    
        nums.sort()     #有重复元素一定要排序，这里的状态变量是start
        res = []
        track = []
        dfs(0)
        return res
# @lc code=end

