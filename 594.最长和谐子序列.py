'''
Author: Zhou Hao
Date: 2021-02-24 23:20:54
LastEditors: Zhou Hao
LastEditTime: 2021-02-25 00:17:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    
    '''hashtable'''
    # def findLHS(self, nums: List[int]) -> int:
        # from collections import Counter
        # hashmap = Counter(nums)
        # if len(hashmap) == 1: return 0


        # res = 0
        # for k,v in hashmap.items():
        #     # print()
        #     if hashmap[k+1] != 0:
        #         res = max(res,v + hashmap[k+1])
        # return res
        


    '''sort  + double pointers'''
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        res=0
        for right in range(len(nums)):
            while nums[right]-nums[left]>1:
                left+=1
            if nums[right]-nums[left]==1:
                res=max(res,right-left+1)
        return res







# @lc code=end

