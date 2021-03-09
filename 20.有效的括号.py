'''
Author: Zhou Hao
Date: 2020-12-19 18:37:42
LastEditors: Zhou Hao
LastEditTime: 2021-03-07 13:55:30
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    
    # def isValid(self, s: str) -> bool:  #返回布尔
    #     #只判断正确的。太暴力了
    #     while '{}' in s or '()' in s or '[]' in s:
    #         s = s.replace('{}', '')
    #         s = s.replace('[]', '')
    #         s = s.replace('()', '')
    #     return s == ''

    
    #栈
    def isValid(self, s: str) -> bool:
        stack = []
    
        pair = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:
            if i in '([{':      #左括号
                stack.append(i)     #入栈
                
            else:       #右括号
                if stack != []:
                    if stack[-1] == pair[i]:
                        stack.pop()     #出栈
                    else:return False
                else:return False

        return  stack == []     #判断是不是空栈
# @lc code=end

