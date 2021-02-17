'''
Author: Zhou Hao
Date: 2021-02-12 22:43:25
LastEditors: Zhou Hao
LastEditTime: 2021-02-13 14:16:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        # print(ord(s))
        res = 0
        times = 0
        while s:
            times += 1
            temp = ord(s[-1])
            s=s[:-1]
            if times != 1:
                res = res+(temp-64)*(26**(times-1))
            elif times == 1:
                res = res + (temp -64)

        return res
# @lc code=end

