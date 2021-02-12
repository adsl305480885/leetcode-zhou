'''
Author: Zhou Hao
Date: 2021-02-08 23:24:25
LastEditors: Zhou Hao
LastEditTime: 2021-02-09 21:59:17
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=788 lang=python3
#
# [788] 旋转数字
#

# @lc code=start
class Solution:
    def rotatedDigits(self, N: int) -> int:
        res = 0
        for i in range(1,N+1,1):
            a = all(s not in '347' for s in str(i))
            b = any(s in '2569' for s in str(i))
            if a and b :
                res +=1
        # print(res )
        return res
# @lc code=end

