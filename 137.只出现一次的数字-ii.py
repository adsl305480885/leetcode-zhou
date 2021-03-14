'''
Author: Zhou Hao
Date: 2021-03-14 20:31:54
LastEditors: Zhou Hao
LastEditTime: 2021-03-14 20:43:55
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
class Solution:
    #hashmap,时间O(n),空间O(n)
    # def singleNumber(self, nums: List[int]) -> int:
    #     from  collections import Counter
    #     count = Counter(nums)
    #     return min(count,key=count.get)

    #hashset  时间O(n),空间O(n)
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums))//2

        
# @lc code=end

