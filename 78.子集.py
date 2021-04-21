'''
Author: Zhou Hao
Date: 2021-04-21 15:41:03
LastEditors: Zhou Hao
LastEditTime: 2021-04-21 16:03:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    '''迭代'''
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
    #     for i in nums:
    #         res = res + [[i] + num for num in res]
    #         print(res)
    #     return res

        

    '''回溯dfs'''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length == 0:return [nums]

        def dfs(start):
            res.append(track[:])
            if start >= length:return

            for i in range(start,length):
                track.append(nums[i])
                dfs(i+1)
                track.pop()


        res = []
        track = []
        dfs(0)
        return res
        
# @lc code=end

