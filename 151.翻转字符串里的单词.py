'''
Author: Zhou Hao
Date: 2021-01-10 13:39:17
LastEditors: Zhou Hao
LastEditTime: 2021-01-10 13:47:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
        

        
# @lc code=end

