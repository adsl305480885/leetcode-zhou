'''
Author: Zhou Hao
Date: 2021-02-05 16:24:22
LastEditors: Zhou Hao
LastEditTime: 2021-02-05 16:30:21
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right = 1,n
        while left <= right:
            mid = (left+right) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left  = mid +1
            elif guess(mid) == -1:
                right = mid -1
        
# @lc code=end

