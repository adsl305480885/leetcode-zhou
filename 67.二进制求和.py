'''
Author: Zhou Hao
Date: 2021-01-06 21:25:11
LastEditors: Zhou Hao
LastEditTime: 2021-01-06 21:28:16
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]   #转数字做的
# @lc code=end

