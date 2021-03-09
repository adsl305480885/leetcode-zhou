'''
Author: Zhou Hao
Date: 2021-03-09 20:11:14
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 20:31:05
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1003 lang=python3
#
# [1003] 检查替换后的词是否有效
#

# @lc code=start
class Solution:

    #方法一:replace()
    # def isValid(self, s: str) -> bool:
        # while 'abc' in s:
        #     s = s.replace('abc','')
        # return s==''



    #方法二:栈
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     for i in s:
    #         stack.append(i)

    #         while len(stack)>=3 and ''.join(stack[-3:]) == 'abc':
    #             stack.pop()
    #             stack.pop()
    #             stack.pop()

    #     return stack == []

        
    def isValid(self, s: str) -> bool:
        new_str = ''

        for i in s:
            new_str +=i
            while new_str[-3:]=='abc':
                new_str = new_str[:-3]

        # print(new_str)
        # print(new_str == '')
        return new_str == ''

# @lc code=end

