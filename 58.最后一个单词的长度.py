'''
Author: Zhou Hao
Date: 2021-01-11 14:17:52
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 14:24:39
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.isspace() == True:
            return 0
        s_new = s.split()[-1]
        return len(s_new)
        
# @lc code=end

