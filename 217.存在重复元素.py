'''
Author: Zhou Hao
Date: 2021-01-20 11:23:47
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 16:06:13
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    '''方法一:哈希,时间复杂度很高''' 
    # def containsDuplicate(self, nums: List[int]) -> bool:  
        # from collections import Counter
        # times = Counter(nums)
        # print(times)
        # print(len(times),len(nums))
        
        # if len(times)<len(nums):
        #     return True
        # else:
        #     return False
        
        
    '''方法二:'''
    def containsDuplicate(self, nums: List[int]) -> bool:  
        if len(set(nums))<len(nums):    #集合去重判断长度
            return True
        else:
            return False
            
    


        
# @lc code=end

