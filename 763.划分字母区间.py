'''
Author: Zhou Hao
Date: 2021-03-16 22:12:49
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 22:37:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    '''贪心'''
    def partitionLabels(self, S: str) -> List[int]:
        hashmap = {}
        for i,s in  enumerate(S):
            hashmap[s] = i      #记录每个字符最后出现的位置

        print(hashmap)
        start = 0
        end = 0
        res = []
        for index,s in enumerate(S):
            end = max(end,hashmap[s])   #如果当前字符的后边界大于以前的，就扩展边界
            
            if index == end:
                res.append(index-start+1)
                start = index +1

        return res
# @lc code=end

