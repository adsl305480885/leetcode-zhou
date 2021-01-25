'''
Author: Zhou Hao
Date: 2021-01-24 14:34:45
LastEditors: Zhou Hao
LastEditTime: 2021-01-24 14:49:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

# @lc code=start
class Solution:
    '''方法一:找出最大的，然后遍历比较'''
    # def dominantIndex(self, nums: List[int]) -> int:
    #     max_num = max(nums)
    #     i = 0 
    #     while i < len(nums):
    #         if nums[i] != max_num:
    #             if max_num >= nums[i]*2:
    #                 i+=1
    #             else:
    #                 return -1
    #         else:
    #             i+=1   #遍历到最大数的时候就跳过
                
        return nums.index(max_num)

    
    '''方法二:思路同方法一，优化了代码'''
    def dominantIndex(self, nums):
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):   #结合all()和列表推导式
            return nums.index(m)
        return -1
        
# @lc code=end

