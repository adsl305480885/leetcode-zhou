'''
Author: Zhou Hao
Date: 2021-04-14 14:49:56
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 15:14:51
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1170 lang=python3
#
# [1170] 比较字符串最小字母出现频次
#

# @lc code=start
from typing import List


class Solution:
    def f(self,strs):
        return strs.count(min(strs))

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = [0] * len(queries)
        f_W = [self.f(w) for w in words]
        
        for i in range(len(queries)):
            f_q = self.f(queries[i])

            ans[i] = sum(w > f_q for w in f_W)

        return ans
        

# @lc code=end

