# @before-stub-for-debug-begin
from python3problem415 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: Zhou Hao
Date: 2021-01-10 11:40:10
LastEditors: Zhou Hao
LastEditTime: 2021-01-10 12:19:32
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
class Solution:
    '''法一：周豪土方，暴力违规'''
    # def addStrings(self, num1: str, num2: str) -> str:
    #     return str(int(num1)+int(num2))
    ''''''


    '''法二：无int(),标准答案'''
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        res = ""
        carry = 0
        while i >=0 or j >= 0:
            #ord()字符串转asic码
            #chr()asic码转字符串
            n1 = num1[i] if i >= 0 else '0'
            n2 = num2[j] if j >= 0 else '0'
            temp = ord(n1) + ord(n2) - 2*ord('0') + carry
            cur = temp%10 
            carry = temp//10
            res = chr(cur+48) + res
            i -= 1
            j -= 1 
        return '1' + res if carry != 0 else res


# @lc code=end

