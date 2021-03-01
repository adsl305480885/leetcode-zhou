'''
Author: Zhou Hao
Date: 2021-03-01 15:26:56
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 15:55:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        hash_ab = {}
        hash_dc = {}
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                temp_ab = A[i] + B[j]
                temp_cd = C[i] + D[j]

                hash_ab[temp_ab] = hash_ab.get(temp_ab,0) +1
                hash_dc[temp_cd] = hash_dc.get(temp_cd,0) +1

        for k,v in hash_ab.items():
            if -k in hash_dc:
                res += v*hash_dc[-k]

        return res
# @lc code=end

