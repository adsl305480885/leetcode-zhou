'''
Author: Zhou Hao
Date: 2021-05-06 15:55:30
LastEditors: Zhou Hao
LastEditTime: 2021-05-06 16:07:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1347 lang=python3
#
# [1347] 制造字母异位词的最小步骤数
#

# @lc code=start
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        count_s = Counter(s)
        count_t = Counter(t)
        a = count_t-count_s
        return sum(a.values())
        
# @lc code=end

