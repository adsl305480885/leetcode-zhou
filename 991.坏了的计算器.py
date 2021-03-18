'''
Author: Zhou Hao
Date: 2021-03-18 10:58:11
LastEditors: Zhou Hao
LastEditTime: 2021-03-18 16:11:15
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=991 lang=python3
#
# [991] 坏了的计算器
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        #逆向思维
        #Y只能除以2或者+1
        res = 0
        while X < Y:            #贪心
            if Y % 2 == 1:  #Y是奇数就加一
                Y += 1
            else:
                Y //= 2
            res += 1
        return res + (X - Y)    #其余的差距，只能一个一个来


# @lc code=end

