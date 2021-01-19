'''
Author: Zhou Hao
Date: 2021-01-12 11:30:34
LastEditors: Zhou Hao
LastEditTime: 2021-01-12 12:52:33
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    '''法一：
    如果s中包含重复的子字符串，那么说明s中至少包含两个子字符串，
    s+s至少包含4个字串，
    前后各去掉一位，查找s是否在新构建的字符串中。'''
    # def repeatedSubstringPattern(self, s: str) -> bool:
        # return s in (s+s)[1:-1]
        

    '''法二:正则'''
    def repeatedSubstringPattern(self, s: str) -> bool:
        import re

        if re.fullmatch(r'([a-z]+)\1+',s):
            print(re.fullmatch(r'([a-z]+)\1+',s))
            return True
        else:
            return False
        
# @lc code=end

