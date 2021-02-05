'''
Author: Zhou Hao
Date: 2021-02-05 14:26:06
LastEditors: Zhou Hao
LastEditTime: 2021-02-05 14:31:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1

        while left <= right:
            mid = (left+right) //2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1
        
# @lc code=end

