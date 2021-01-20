'''
Author: Zhou Hao
Date: 2021-01-20 16:09:41
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 16:38:28
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    
    '''方法一:双指针,
            当左指针0，右指针非0， 替换，左右指针同时右移
            左指针0，右指针0，右指针右移，直到右指针非0
            左指针非0，左右指针同时右移

            用左指针寻找0元素，右指针寻找非0元素，然后互换
            只需要遍历一遍数组，O(n)
    '''
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,1
        while j < len(nums):
            if nums[i] ==0 and nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j += 1
            elif nums[i] ==0 and nums[j] == 0:
                j += 1
                
            # elif nums[i] !=0 and nums[j] != 0:
            #     i+=1
            #     j+=1
            # elif nums[i] !=0 and nums[j] == 0:
            #     i+=1
            #     j+=1
            else:
                i+=1
                j+=1


# @lc code=end

