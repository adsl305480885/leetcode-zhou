'''
Author: Zhou Hao
Date: 2021-03-07 23:33:49
LastEditors: Zhou Hao
LastEditTime: 2021-03-07 23:44:07
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_S,stack_T = [],[]

        for i in range(len(S)):
            if S[i] == '#':
                if stack_S != []:
                    stack_S.pop()
            else:stack_S.append(S[i])

        for i in range(len(T)):
            if T[i] == '#':
                if stack_T != []:
                    stack_T.pop()
            else:stack_T.append(T[i])

        # print(stack_S,stack_T)
        return stack_S == stack_T
# @lc code=end

