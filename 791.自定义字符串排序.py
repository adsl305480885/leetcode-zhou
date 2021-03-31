'''
Author: Zhou Hao
Date: 2021-03-31 19:03:18
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 19:58:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=791 lang=python3
#
# [791] 自定义字符串排序
#

# @lc code=start
class Solution:
    #hashmap
    # def customSortString(self, S: str, T: str) -> str:
    #     hashmap_T = {}
    #     for t in T:
    #         hashmap_T[t] =hashmap_T.get(t,0)+1


    #     res = ''
    #     for s in S:
    #         if s not in hashmap_T:
    #             continue
    #         while hashmap_T[s] != 0:
    #             res +=s
    #             hashmap_T[s] -= 1

    #     for k,v in hashmap_T.items():
    #         if v != 0:
    #             while v != 0:
    #                 res += k
    #                 v -= 1


    #     return res
        
        
    def customSortString(self, S: str, T: str) -> str:
        import collections
        cs = collections.Counter(S)
        ct = collections.Counter(T)
        return ''.join(list((cs+ct-cs).elements()))
# @lc code=end

