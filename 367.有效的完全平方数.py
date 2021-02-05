'''
Author: Zhou Hao
Date: 2021-02-05 16:14:58
LastEditors: Zhou Hao
LastEditTime: 2021-02-05 16:22:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left ,right = 1,num

        while left <=right:
            mid = (left+right) // 2
            if mid*mid == num:
                return True
            elif mid*mid <num:
                left = mid+1
            elif mid*mid > num:
                right = mid -1
        return False
        
# @lc code=end

