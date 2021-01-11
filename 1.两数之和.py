'''
Author: Zhou Hao
Date: 2021-01-11 13:54:11
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 14:15:58
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    '''方法一：哈希字典'''
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    #     hashmap = {}
    #     for index,num in enumerate(nums):
    #         hashmap[num] = index   #列表的值是键，列表的索引是值

    #     for i, num in enumerate(nums):
    #         j = hashmap.get(target-num)     #根据字典键获取值
    #         if j is not None and j !=i:
    #             return[i,j]


    '''方法二:O(n)'''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            digits = target-num
            if digits in nums[i:] and nums.index(digits) != i:
                return [i,nums.index(digits)]
            
            


# @lc code=end

