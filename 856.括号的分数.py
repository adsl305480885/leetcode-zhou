'''
Author: Zhou Hao
Date: 2021-03-08 11:55:45
LastEditors: Zhou Hao
LastEditTime: 2021-03-08 13:35:08
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] 括号的分数
#

# @lc code=start
class Solution:
    #栈
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for i in S:
            print(stack)
            if i == "(":
                stack.append(i)

            else:
                temp = 0
                #如果是左括号，直接放进去
                if stack[-1] =="(":
                    temp +=1
                    stack.pop()
                    stack.append(temp)
                else:
                    #把中间的值加起来，然后乘以2，再放进栈
                    while stack[-1] !="(":
                        temp += stack.pop()
                    stack.pop()
                    stack.append(2*temp)

        return sum(stack)
# @lc code=end

