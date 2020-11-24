#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#
import re

# @lc code=start
class Solution:

    '''指针法'''
    # def findOcurrences(self, text: str, first: str, second: str) -> list:
    #     if len(text) > 1000 or len(text) <1:
    #         return  ['False']

    #     tokenlist = text.split()     #根据空格切割每个单词
    #     res = []
    #     for i in range(1,len(tokenlist)):
    #         if tokenlist[i-1] == first  and tokenlist[i] == second and i+1<len(tokenlist):
    #             res.append(tokenlist[i+1])
        
    #     return res 


    '''正则'''
    def findOcurrences(self, text: str, first: str, second: str) -> list:
        return re.findall(fr"(?<=\b{first} {second} )(\w+)", text)

    '''栈'''

# @lc code=end

