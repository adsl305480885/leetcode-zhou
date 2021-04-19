'''
Author: Zhou Hao
Date: 2021-03-01 14:04:55
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 15:59:13
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
from typing import List


class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     hashmap = {}
    #     res = 0

    #     count = 0
    #     for n in nums:
    #         count += n
    #         # hashmap[count]= hashmap.get(count,0)+1
    #         # print(hashmap,count)
    #         if count == k:
    #             # print('aaa')
    #             res+=1
    #         if count-k in hashmap:
    #             # print('bbb') 
    #             res += hashmap[count-k]

    #         hashmap[count]= hashmap.get(count,0)+1
    #         # print(hashmap,count)
    #     return res
        

    '''前缀和'''
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        '''前缀后数组'''
        # length = len(nums)
        # presum = [0] * (length+1)       #首位置0 
        # for i in range(length):
        #         presum[i+1] = nums[i] + presum[i]
        # print(presum)


        '''前缀和哈希 O(n)'''
        presum = {0:1}
        res = 0
        sum_i = 0
        length = len(nums)

        for i in range(length):
            sum_i += nums[i]    #前缀和
            sum_j = sum_i - k
            if sum_j in presum:
                res += presum[sum_j]
            presum[sum_i] = presum.get(sum_i,0)+1

        return res

# @lc code=end

