'''
Author: Zhou Hao
Date: 2021-04-14 19:41:02
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 19:54:55
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#

# @lc code=start
class Solution:

    '''滑动窗口'''
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,right = 0,0
        res = 0
        count_0 = 0

        while right < len(nums):
            if nums[right] == 0:
                count_0 += 1

            while count_0 > k:      #注意边界条件
                if nums[left] == 0:
                    count_0 -= 1
                left += 1
            res = max(res,right-left + 1)

            right += 1

        return res
# @lc code=end

