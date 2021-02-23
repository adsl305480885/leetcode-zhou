'''
Author: Zhou Hao
Date: 2021-02-23 13:25:19
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 14:57:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    '''
        hash找出重复数字
        集合找出缺失数字
    '''
    # def findErrorNums(self, nums: List[int]) -> List[int]:
        # import collections
        # times = collections.Counter(nums)
        # double = max(times,key =times.get)
        # set1 = set(nums)
        # set2 = set(range(1,len(nums)+1))
        # return [double,(set2-set1).pop()]


    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = {}
        double = 0
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]]=1
            else:
                double = nums[i]
                break
        
        n = sum(range(1,len(nums)+1)) -sum(nums) + double   #数学推导
        # print(n,double)
        return [double,n]
# @lc code=end

