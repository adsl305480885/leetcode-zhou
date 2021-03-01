'''
Author: Zhou Hao
Date: 2021-03-01 14:04:55
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 15:04:14
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {}
        res = 0

        count = 0
        for n in nums:
            count += n
            # hashmap[count]= hashmap.get(count,0)+1
            # print(hashmap,count)
            if count == k:
                # print('aaa')
                res+=1
            if count-k in hashmap:
                # print('bbb') 
                res += hashmap[count-k]

            hashmap[count]= hashmap.get(count,0)+1
            # print(hashmap,count)
        return res
# @lc code=end

