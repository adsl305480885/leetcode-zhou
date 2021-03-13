'''
Author: Zhou Hao
Date: 2021-03-13 14:47:29
LastEditors: Zhou Hao
LastEditTime: 2021-03-13 15:03:53
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        #栈解决,把当前目录压入栈中,遇到..弹出栈顶,最后返回栈中元素.
        stack = []

        path = path.split('/')
        # print(path)
        for p in path:
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p!= '.':
                stack.append(p)
        # print('/'+'/'.join(stack))
        return '/'+'/'.join(stack)
# @lc code=end

