'''
Author: Zhou Hao
Date: 2021-03-12 16:48:57
LastEditors: Zhou Hao
LastEditTime: 2021-03-13 14:03:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    # eval 字符串转表达式
    # def calculate(self, s: str) -> int:
    #     s = ''.join([ i if i!='/' else '//' for i in s ])
    #     return eval(s)
        

    #双栈
    # def calculate(self, s: str) -> int:
    #     #先乘除再加减
    #     stack = []      #先格式化字符串，方便后面计算
    #     for i in s:
    #         if i in '+-*/':
    #             stack.append(i)
    #         else:
    #             if i == ' ':
    #                 continue
    #             if (not stack) or (stack[-1] in '+-*/') :
    #                 stack.append(i)
    #             elif stack[-1].isdigit() :
    #                 stack[-1] += i

    #     import operator
    #     options = {
    #         '+':operator.add,
    #         '-':operator.sub,
    #         '*':operator.mul,
    #         '/':operator.floordiv
    #     }
    #     stack_num ,stack_opt = [],[]

    #     #算乘除
    #     for i in stack:
    #         if i.isdigit():
    #             stack_num.append(int(i))

    #             if stack_opt!= [] and stack_opt[-1] in '/*':
    #                 temp = options[stack_opt[-1]](stack_num[-2], stack_num[-1])
    #                 print('temp\t',temp,'\ti:',i)
    #                 stack_num.pop()
    #                 stack_opt.pop()
    #                 stack_num[-1] = temp
    #         elif i!= ' ':
    #             stack_opt.append(i)
            
            
    #     #加减
    #     i,j,res= 0,0,0
    #     while i <len(stack_num)-1 and j<len(stack_opt):
    #         temp = options[stack_opt[j]](stack_num[i],stack_num[i+1])
    #         stack_num[i+1] = temp
    #         i+=1
    #         j+=1
        
    #     return stack_num[-1]





    #双栈
    def calculate(self, s: str) -> int:
        stack = []
        for i in s:
            if i in '+-*/':
                stack.append(i)
            else:
                if i == ' ':
                    continue
                if (not stack) or (stack[-1] in '+-*/') :
                    if stack and  stack[-1]=='-':
                        stack[-1] = '+'
                        stack.append('-'+i)     #把减法换成负数
                    else:
                        stack.append(i)
                elif stack[-1].isdigit() or int(stack[-1]) <0  :
                    stack[-1] += i

        # print(stack)
        import operator
        options = {
            '+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.floordiv
        }
        stack_num ,stack_opt = [],[]

        #算乘除
        for i in stack:
            if i not in '+*/':
                stack_num.append(int(i))

                if stack_opt!= [] and stack_opt[-1] in '/*':
                    if stack_opt[-1] == '/':
                        temp = int(stack_num[-2]/stack_num[-1])   #除法保留整数
                    else:
                        temp = options[stack_opt[-1]](stack_num[-2], stack_num[-1])

                    stack_num.pop()
                    stack_opt.pop()
                    stack_num[-1] = temp
            elif i!= ' ':
                stack_opt.append(i)
        return sum(stack_num)           #直接返回和,减法就是负数
# @lc code=end

