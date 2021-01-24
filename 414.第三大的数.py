'''
Author: Zhou Hao
Date: 2021-01-21 14:28:33
LastEditors: Zhou Hao
LastEditTime: 2021-01-21 14:59:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

# @lc code=start
class Solution:

    '''方法一:
        集合去重，降序排序，输出第三大的数，
        注意长度
    '''
    # def thirdMax(self, nums: List[int]) -> int:
    #     if len(nums) <= 2:return max(nums)
            
    #     nums = list(set(nums))
    #     new_nums = sorted(nums,reverse=True)

    #     if len(new_nums) >=3:return new_nums[2]
    #     return  max(new_nums)
        



    '''方法二:'''
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        nums = set(nums)

        if len(nums) < 3:
            return max(nums)


        for  i in range(2):
            max_nums = max(nums)
            nums.remove(max_nums)

        print(nums)
        return max(nums)
        
    

# @lc code=end

