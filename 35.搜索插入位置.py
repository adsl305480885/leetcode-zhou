'''
Author: Zhou Hao
Date: 2021-01-20 09:59:45
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 10:44:32
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    '''遍历'''
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     else:
    #         if max(nums) < target:
    #             return len(nums)
    #         elif min(nums) >target:
    #             return 0
    #         else:
    #             for i in range(len(nums)):
    #                 if nums[i]<target<nums[i+1]:
    #                     return i+1
                        

    '''递归二分查找'''
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binaryseach(nums,left,right,x):
            mid = int((left+right)/2)
            if x < nums[mid]:
                if nums[mid-1] < x:return mid   
                return binaryseach(nums,left,mid-1,x)
            elif x > nums[mid]:
                if nums[mid+1]>x:return mid+1
                return binaryseach(nums,mid+1,right,x)


        if target in nums:
            return nums.index(target)
        else:
            if max(nums) < target:
                return len(nums)
            elif min(nums) >target:
                return 0
            else:
                #在升序数组中进行二分查找
                return binaryseach(nums,0,len(nums)-1,target)
# @lc code=end

