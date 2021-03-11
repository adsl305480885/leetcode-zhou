'''
Author: Zhou Hao
Date: 2021-03-10 20:43:59
LastEditors: Zhou Hao
LastEditTime: 2021-03-10 21:35:33
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1190 lang=python3
#
# [1190] 反转每对括号间的子串
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        num = 0 

        for i in s:
            if not stack or i=='(' :
                stack.append('')

            if i.isalpha():
                stack[-1] += i      #字符串相加
            # elif i =='(' :
            #     stack.append('')
                # num += 1
            elif i ==')':
                if len(stack) >1:
                    stack[-2] = stack[-2]+stack[-1][::-1]
                    stack.pop()
                else:
                    stack[-1] = stack[-1][::-1]
            # print(stack)
        return stack[0]
# @lc code=end

