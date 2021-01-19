'''
Author: Zhou Hao
Date: 2021-01-17 17:18:03
LastEditors: Zhou Hao
LastEditTime: 2021-01-17 17:38:19
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    '''方法一:双指针'''
    # def reverseOnlyLetters(self, S: str) -> str:
    #     left , right = 0,len(S)-1
    #     S = list(S)
    #     while left < right:
    #         if S[left].isalpha() and S[right].isalpha():
    #             S[left],S[right] = S[right],S[left]
    #             left +=1 
    #             right -=1
                
    #         elif not S[left].isalpha():
    #             left += 1
    #         elif not S[right].isalpha():
    #             right -= 1

    #     return ''.join(S)
            
            

    '''方法二:栈'''
    def reverseOnlyLetters(self, S: str) -> str:
        alphas = [a for a in S if a.isalpha()]

        resutl = []

        for s in S:
            if s.isalpha():
                resutl.append(alphas.pop())#翻转字母就是出栈
            else:resutl.append(s)

        return ''.join(resutl)


        
        
# @lc code=end

