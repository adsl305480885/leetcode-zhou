'''
Author: Zhou Hao
Date: 2021-02-24 21:18:32
LastEditors: Zhou Hao
LastEditTime: 2021-02-24 21:25:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = {}

        for i in arr:
            if i not in  hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        # print(len(set(hashmap.values())) == len(hashmap.values()))
        return len(set(hashmap.values())) == len(hashmap.values())
# @lc code=end

