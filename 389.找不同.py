'''
Author: Zhou Hao
Date: 2021-02-23 00:10:57
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 09:22:54
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    '''hashtable'''
    # def findTheDifference(self, s: str, t: str) -> str:
    #     hashmap = {}
    #     for i in range(len(t)):
    #         if t[i] not in hashmap:hashmap[t[i]] = 1
    #         else:hashmap[t[i]] += 1
    #     # print(hashmap)

    #     for i in range(len(s)):
    #         if s[i] in hashmap:
    #             hashmap[s[i]] -= 1
    #         # else:hashmap[s[i]] += 1
    #         if  hashmap[s[i]] ==0:
    #             del hashmap[s[i]]
    #     # print([k for k,v in hashmap.items() if v==1][0])
    #     for k,v in hashmap.items():
    #         return k

    '''数次数，单数的就是不同的'''
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        new1 = s+t
        a = Counter(new1)
        # print(a)
        for k,v in a.items():
            if v%2!=0:
                # print(k)
                return k
# @lc code=end

