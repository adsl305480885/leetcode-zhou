'''
Author: Zhou Hao
Date: 2021-04-28 11:09:36
LastEditors: Zhou Hao
LastEditTime: 2021-04-28 11:21:23
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=893 lang=python3
#
# [893] 特殊等价字符串组
#

# @lc code=start
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:

        hashset = set()

        for i in  range(len(A)):
            ji,ou = [],[]
            for j in range(len(A[i])):
                if j%2 == 0: ji.append( A[i][j])
                else: ou.append(A[i][j])

            ji = sorted(ji)
            ou = sorted(ou)
            hashset.add(''.join(ji+ou))

        return len(hashset)
        
# @lc code=end

