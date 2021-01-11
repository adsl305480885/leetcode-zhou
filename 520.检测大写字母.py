'''
Author: Zhou Hao
Date: 2021-01-11 20:22:45
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 20:26:43
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.capitalize() \
        or word == word.upper() or word == word.lower():
            return True
        else:return False
# @lc code=end

