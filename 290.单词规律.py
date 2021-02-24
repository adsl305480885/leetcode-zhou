'''
Author: Zhou Hao
Date: 2021-02-24 21:29:11
LastEditors: Zhou Hao
LastEditTime: 2021-02-24 22:17:28
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern ) != len(s):return False
        
        dic_p,dic_s = {},{}
        for i in range(len(pattern)):
            if (pattern[i] in dic_p and dic_p[pattern[i]] != s[i])  or \
                (s[i] in dic_s and  dic_s[s[i]] != pattern[i]):
                return False
            dic_p[pattern[i]] = s[i]
            dic_s[s[i]] = pattern[i]

            print(dic_p,dic_s)

        print(dic_p,'\n',dic_s)
        return True
        
# @lc code=end

