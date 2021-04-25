'''
Author: Zhou Hao
Date: 2021-03-07 23:04:51
LastEditors: Zhou Hao
LastEditTime: 2021-03-07 23:23:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#

# @lc code=start
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        ops = [ int(o) if o.isdigit() or '-' in o else o for o in ops ]
        # print(ops)
        for o in ops:
            # print(stack)
            if o == 'C':
                stack.pop()     #出栈
            elif o == 'D':  
                stack.append(2*stack[-1])   #入栈
            elif o == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(o)


        # print(stack)
        return sum(stack)
# @lc code=end

