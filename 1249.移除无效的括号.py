'''
Author: Zhou Hao
Date: 2021-03-10 15:28:47
LastEditors: Zhou Hao
LastEditTime: 2021-03-10 20:43:34
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:

    #双栈
    # def minRemoveToMakeValid(self, s: str) -> str:
        # stack = []     #栈中只记录需要删除的(的索引
        # right = []  #记录需要删除的)的索引
        # s= list(s)

        # #从左到右 删除多余的)
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)     #左括号索引入栈
        #     elif s[i] == ')':
        #         if stack:
        #             stack.pop()     #出栈,合法的()抵消了。
        #         else:
        #             right.append(i)
                    

            
        # remove = stack+right
        # # print(remove)
        # res = ''
        # for i,v in enumerate(s):
        #     if i not in remove:
        #         # print(v)
        #         res += v

        # # print(res)
        # return res
        
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        num = 0

        #从左到右遍历，确保里面的)都是合法的,去除多余的)
        for i in s:
            if i == '(':
                stack.append(i)
                num += 1        #计算(的数量
            elif i.isalpha():
                stack.append(i)
            elif i == ')':
                if num >0:      #判断是否合法
                    stack.append(i)     #合法)入栈
                    num -= 1    #(的数量减一
        
        # print(stack,num)
        #从右到左遍历，去除多月的(
        stack_right = []
        num_right = 0
        for i in stack[::-1]:
            if i == ')':
                stack_right.append(i)
                num_right += 1
            if i.isalpha():
                stack_right.append(i)
            elif i =='(' and num_right>0:
                stack_right.append(i)
                num_right -=1

        # print(stack_right,num_right)
        # print(''.join(stack_right[::-1]))
        return ''.join(stack_right[::-1])
# @lc code=end

