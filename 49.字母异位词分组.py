'''
Author: Zhou Hao
Date: 2021-02-23 23:01:00
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 23:38:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_origin = strs
        strs = [''.join(sorted(s)) for s in strs]  #排序后转为字符串,把字母异位词转为相同顺序的字符串
        hashmap = {}    #哈希表记录每个字符串的索引

        for index,s in enumerate(strs):
            if s not in hashmap:
                hashmap[s] = [index]
            else:
                hashmap[s].append(index)

        res = []

        for v in  hashmap.values():
            res.append([strs_origin[i] for i in v  ])
        return res

# @lc code=end

