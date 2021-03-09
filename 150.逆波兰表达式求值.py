'''
Author: Zhou Hao
Date: 2021-03-09 12:55:07
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 13:42:37
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    # def evalRPN(self, tokens: List[str]) -> int:
    #     #后缀表达式
    #     stack = []

    #     for t in tokens:
    #         if t in '+-/*':
    #             temp = str(int(eval(stack[-2]+t+stack[-1])))
    #             # print(temp)
    #             stack.pop()
    #             stack.pop()
    #             stack.append(temp)
    #         else :
    #             stack.append(t)
        
    #         # print(stack)
            
    #     return int(stack[0])

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        import operator
        options = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.truediv
        }

        for t in tokens:
            if t in '+-/*':
                temp = int(options[t](stack[-2],stack[-1])) #除法取整数部分
                # print(temp)
                stack.pop()
                stack.pop()
                stack.append(temp)
            else :
                stack.append(int(t))

        return stack[0]
# @lc code=end

