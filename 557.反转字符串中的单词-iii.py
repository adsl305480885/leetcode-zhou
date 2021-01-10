'''
Author: Zhou Hao
Date: 2021-01-10 13:52:58
LastEditors: Zhou Hao
LastEditTime: 2021-01-10 14:16:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        result = ''
        for i in s.split():
            i = i[::-1]
            result += (i+' ')
            
        return result[:-1]

        
        
# @lc code=end

