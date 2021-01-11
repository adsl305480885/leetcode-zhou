'''
Author: Zhou Hao
Date: 2021-01-11 20:07:20
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 20:21:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    '''法一:掉包'''
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if not needle: return 0
    #     if needle not in haystack:return-1
    
    #     return haystack.find(needle)

    '''方法二：滑动窗口'''
    def strStr(self, haystack: str, needle: str) -> int:
        len1 = len(haystack)
        len2 = len(needle)
        for i in range(len1-len2+1):
            if haystack[i:i+len2] == needle:
                return i
        return -1


        

    
# @lc code=end

