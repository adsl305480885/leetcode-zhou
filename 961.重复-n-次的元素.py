'''
Author: Zhou Hao
Date: 2021-02-24 20:39:56
LastEditors: Zhou Hao
LastEditTime: 2021-02-24 20:48:37
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 重复 N 次的元素
#

# @lc code=start
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashmap = {}

        for a in A:
            if a not in hashmap:
                hashmap[a] = 1
            else:
                # hashmap[a] += 1
                return a

            
# @lc code=end

