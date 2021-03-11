'''
Author: Zhou Hao
Date: 2021-03-11 16:06:26
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 16:14:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    
    #可以通过翻转得到另一张，就把大的当十位小的当个位，找相同
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for index,[i,j] in enumerate(dominoes):
            # print(i,j)
            dominoes[index] = i*10 +j if i>=j else j*10+i

        from collections import Counter
        # print(dominoes)
        count = Counter(dominoes)
        # print(count)
        res = 0
        for v in count.values():
            res += v*(v-1) / 2
        return int(res)
# @lc code=end

