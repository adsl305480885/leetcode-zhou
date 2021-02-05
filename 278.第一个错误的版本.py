'''
Author: Zhou Hao
Date: 2021-02-05 13:40:44
LastEditors: Zhou Hao
LastEditTime: 2021-02-05 14:22:01
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    #二分法，当left和right 的值相等，此时它们就表示了第一个错误版本的位置
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right = 1,n
        while left < right:
            mid = (left+right)//2
            if not isBadVersion(mid):       #正确版本,mid之前（包含mid）都是对的
                left = mid+1
            else:                   #错误版本，mid之后(包含mid)都是错的
                right = mid

        
        return left

        
        
        
# @lc code=end

