'''
Author: Zhou Hao
Date: 2021-01-29 22:26:23
LastEditors: Zhou Hao
LastEditTime: 2021-01-30 16:09:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1

        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid       #由于是向下取，所以应该写在这里
                l = mid + 1
            else:
                # ans = mid
                r = mid - 1
            print(mid,l,r,ans)
        return ans
        
# @lc code=end

