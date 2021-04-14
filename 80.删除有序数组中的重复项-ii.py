'''
Author: Zhou Hao
Date: 2021-04-14 20:36:01
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 20:51:33
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    
    '''双指针'''
    def removeDuplicates(self, nums: List[int]) -> int:
        left ,right = 0,0

        while right <len(nums):
            if nums[left] == nums[right]:
                if right - left +1>2:   #pop之后right 不变，
                    nums.pop(right)
                else:
                    right+=1
            else:
                left += 1
                right += 1

        return right


# @lc code=end

