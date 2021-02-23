'''
Author: Zhou Hao
Date: 2021-02-23 21:15:45
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 21:37:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    #排序
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return sorted(s) == sorted(t)


    #哈希
    # def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):return False
        # hashmap = {}
        # for i in s:
        #     if i not in hashmap:
        #         hashmap[i] = 1
        #     else:
        #         hashmap[i] += 1

        # for i in t:
        #     if i not in hashmap or t.count(i) != hashmap[i]:
        #         return False
        # return True
        
        
    #asci
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        if set(s) != set(t):return False
        
        sum_s,sum_t = 0,0
        for i in range(len(s)):
            sum_s += ord(s[i])
            sum_t += ord(t[i])
        return sum_s == sum_t
# @lc code=end

