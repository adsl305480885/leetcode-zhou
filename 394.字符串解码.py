'''
Author: Zhou Hao
Date: 2021-03-08 09:42:26
LastEditors: Zhou Hao
LastEditTime: 2021-03-08 11:33:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
class Solution:
    
    #栈,死暴力笨方法 ,一次遍历O(n)
    # def decodeString(self, s: str) -> str:
    #     stack = []      
    #     i = 0
    #     res = ''
    #     while i <len(s):
    #         temp = ''
            
    #         if s[i].isdigit():
    #             if stack == [] or not stack[-1].isdigit():
    #                 stack.append(s[i])
    #             else:
    #                 if s[i-1] == '[':
    #                     stack.append(s[i]) 
    #                 else:
    #                     stack[-1] += s[i]


    #         elif s[i].isalpha():
    #             if s[i-1] == '[': 
    #                 stack.append(s[i])
    #             else:
    #                 if stack != []:
    #                     stack[-1] = stack[-1] + s[i]
    #                 else:
    #                     res += s[i]


    #         elif s[i] == ']':
    #             temp += stack[-1] * int(stack[-2])
    #             stack.pop()
    #             stack.pop()
    #             if stack != []:
    #                 if not stack[-1].isdigit():
    #                     stack[-1] = stack[-1] + temp
    #                 else:
    #                     stack.append(temp)
    #             else:
    #                 res += temp
                    
    #         i+=1
    #     return res
        
    #大佬方法
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            print(stack)
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res
# @lc code=end

