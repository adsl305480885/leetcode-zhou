'''
Author: Zhou Hao
Date: 2021-02-12 22:24:51
LastEditors: Zhou Hao
LastEditTime: 2021-02-12 22:43:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n -= 1  #重点
            res = chr(n%26 + 65) + res
            n = n//26

        return res
# @lc code=end

