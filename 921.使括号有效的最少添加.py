'''
Author: Zhou Hao
Date: 2021-03-09 18:49:40
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 19:23:41
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=921 lang=python3
#
# [921] 使括号有效的最少添加
#

# @lc code=start
class Solution:
    
    #栈
    # def minAddToMakeValid(self, S: str) -> int:
    #     res = 0
    #     stack = []

    #     for s in S:
    #         if s == '(':
    #             stack.append(s)
    #         else:
    #             if stack :
    #                 stack.pop()
    #             else:res += 1

    #     return len(stack)+res


    #replace()替换
    # def minAddToMakeValid(self, S: str) -> int:
    #     while '()' in S:
    #         S = S.replace('()','')
    #     return len(S)


    #计数法
    def minAddToMakeValid(self, S: str) -> int:
        left = right = 0 # left表示需要补齐的左括号，res表示需要补齐的右括号
        for i in S:
            if i == '(':
                right += 1
            else:
                right -= 1
            
            if right < 0: # 此时说明右括号超过了左括号数
                left += 1       #需要补的左括号数量
                right += 1 # 重置right，左括号已补齐
        
        # print(left + right,left,right)
        return left +right


        
# @lc code=end

