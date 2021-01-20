'''
Author: Zhou Hao
Date: 2021-01-20 10:55:08
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 11:22:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        times = Counter(nums)
        print(times)
        threshold = len(nums)/2
        
        '''方法一:耗时少点'''
        # for k,v in times.items():
        #     if v > threshold:
        #         return k
        
        '''方法二:耗时多点'''
        return max(times,key=times.get)

        
# @lc code=end

