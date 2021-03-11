'''
Author: Zhou Hao
Date: 2021-03-11 13:56:15
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 15:06:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=916 lang=python3
#
# [916] 单词子集
#

# @lc code=start
class Solution:
    #汇总B中所有单词b   O(2n)
    #字典记录B中每个字母出现的最多次数
    #判断A中每个单词是否满足字典中每个字母的次数
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        from collections import Counter
        count_B = {}
        res = []
        for b in B:
            count_b = Counter(b)
            for k,v in count_b.items():
                if k not in count_B:
                    count_B[k] = v
                else:
                    count_B[k] = max(count_B[k],v)


        for a in A:
            count_a = Counter(a)
            # print(count_a)
            for  k,v in count_B.items():
                if not count_a[k] or v > count_a[k]:
                    break
            else:
                res.append(a)
        return res
        
# @lc code=end

