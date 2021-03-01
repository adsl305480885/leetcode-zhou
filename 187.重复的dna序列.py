'''
Author: Zhou Hao
Date: 2021-03-01 15:06:51
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 15:23:01
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    #哈希
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashmap = {}
        # print(len(s))
        res = []
        for i in range(len(s)-9):
            # print(i,s[i:i+10])
            temp = s[i:i+10]
            hashmap[temp] = hashmap.get(temp,0) + 1


        # print(hashmap)
        for k,v in hashmap.items():
            if v>=2:res.append(k)

        # print(res)
        return res
# @lc code=end

