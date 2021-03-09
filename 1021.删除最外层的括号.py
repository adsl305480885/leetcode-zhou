'''
Author: Zhou Hao
Date: 2021-03-07 13:58:17
LastEditors: Zhou Hao
LastEditTime: 2021-03-07 14:13:17
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    # 左括号入栈：若入栈后栈的长度大于1，即该左括号不是原语首个左括号，结果加入'('
    # 右括号出栈：若出栈后栈的长度大于0，即该右括号不是原语末个右括号，结果加入')'
    def removeOuterParentheses(self, S: str) -> str:
        stack,res = [],''
        for i in S:
            if i == '(':
                stack.append(i) #左括号入栈
                if len(stack) >1:       #判断是不是外层的左括号
                    res+= '(' #最外层的括号入栈时，答案不添加括号
            else:
                stack.pop()     #右括号出栈
                if len(stack) >0:       #判断是不是外层的右括号
                    res+= ')'
                    
        return res
# @lc code=end

