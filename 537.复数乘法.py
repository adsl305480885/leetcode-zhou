'''
Author: Zhou Hao
Date: 2021-03-31 21:00:36
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 21:10:18
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_real, a_imag = map(int, a.replace("i", "").split("+"))
        b_real, b_imag = map(int, b.replace("i", "").split("+"))

        # print(a_real,a_imag)

        res = str((a_real * b_real - a_imag * b_imag)) + "+" + str((a_real * b_imag + a_imag * b_real)) + "i"
        
        return res
# @lc code=end

