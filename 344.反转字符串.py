'''
Author: Zhou Hao
Date: 2021-01-07 23:16:42
LastEditors: Zhou Hao
LastEditTime: 2021-01-07 23:30:56
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            #python支持直接换，不用中间变量
            s[i],s[len(s)-1-i] = s[len(s)-1-i] ,s[i]
        
# @lc code=end

