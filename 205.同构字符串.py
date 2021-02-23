#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            if s[i] in hashmap_s:
                if hashmap_s[s[i]] != t[i]: return False
            if t[i] in hashmap_t:
                if hashmap_t[t[i]] != s[i]:return False
            hashmap_s[s[i]] = t[i]
            hashmap_t[t[i]] = s[i]
        return True
# @lc code=end

