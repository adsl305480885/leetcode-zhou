'''
Author: Zhou Hao
Date: 2021-01-12 13:36:38
LastEditors: Zhou Hao
LastEditTime: 2021-01-12 13:55:10
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=521 lang=python3
#
# [521] 最长特殊序列 Ⅰ
#

# @lc code=start
class Solution:
    
    '''
    1.字符串长度不相等：在这种情况下,
    因为字符串本身就是自己的子序列，
    且较长的字符串肯定不能是短的字符串的子序列，
    所以此时较长字符串的长度肯定就是结果
    
    2.字符串长度相等： 此时又分为两种情况，
    第一个为两个字符串完全相同，输出-1，
    另一个两个字符串不相同，
    则此时最长子序列即字符串本身肯定不可能和另一个字符串一样，
    所以输出字符串长度。
    '''
    # def findLUSlength(self, a: str, b: str) -> int:
    #     if a == b:
    #         return -1
    #     n = len(a)
    #     m = len(b)
    #     if len(a) != len(b):
    #         return n if n>m else m
    #     return n
        


    ''''''
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a), len(b))

        
# @lc code=end

