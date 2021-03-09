'''
Author: Zhou Hao
Date: 2021-03-07 15:02:14
LastEditors: Zhou Hao
LastEditTime: 2021-03-07 15:15:22
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    #栈
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for i,s in enumerate(S):
            if i == 0:
                stack.append(s) 
            
            else:
                # print('\t\t\t',stack[-1])
                if stack!= [] and s == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s)
            # print(s,stack)

        # print(''.join(stack))
        return ''.join(stack)
# @lc code=end

