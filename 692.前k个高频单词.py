'''
Author: Zhou Hao
Date: 2021-04-19 21:59:10
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 22:13:21
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#

# @lc code=start
class Solution:

    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}

        for w in words:
            hashmap[w] = hashmap.get(w,0) + 1
        
        hashmap = sorted(hashmap.items(),key=lambda x:(-x[1],x[0]),reverse=False)

        return [i[0] for i in hashmap[:k] ]
# @lc code=end

