# @before-stub-for-debug-begin
from python3problem434 import *
from typing import *
# @before-stub-for-debug-end

'''
Author: Zhou Hao
Date: 2021-01-10 12:19:57
LastEditors: Zhou Hao
LastEditTime: 2021-01-10 12:32:55
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        
        '''法一'''
        # if s.strip()=='':
        #     print(s.strip())
        #     return 0
        # list_s = s.split(" ")
        # print(list_s)
        # list_s_new = [x for x in list_s if x != ""]
        # return len(list_s_new)
        

        '''法二'''
        return len(s.split())
# @lc code=end

