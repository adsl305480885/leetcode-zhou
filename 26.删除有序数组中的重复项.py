'''
Author: Zhou Hao
Date: 2021-04-18 17:04:25
LastEditors: Zhou Hao
LastEditTime: 2021-04-18 17:17:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    
    '''快慢指针'''
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:return 0
        slow,fast = 0,0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        print(nums)

        return slow + 1


# @lc code=end

