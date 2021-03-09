'''
Author: Zhou Hao
Date: 2021-03-09 10:00:59
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 12:54:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        #单调递增栈
        stack = []
        for i in num:
            #在删除K个数字之前,保持单增栈
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        #已经是单增栈了,但是还没有删除K个数字
        while k > 0:
            stack.pop()
            k -= 1

        if stack == []:
            return '0'
        return str(int(''.join(stack)))     #排除前导0
# @lc code=end

