'''
Author: Zhou Hao
Date: 2021-04-19 16:01:18
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 16:54:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#

# @lc code=start
class Solution:
    '''哈希前缀和.key=余数，value=次数'''
    
        #     前缀和

        # sum[i:j] = sum[:j] - sum[:i]

        # 可以被k整除的连续数组，只要保证sum[:j]和sum[:i]的对k的余数相等即可。
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum = {0:1}
        res = 0
        sum_i = 0

        for i in range(len(A)):
            sum_i += A[i]
            sum_i= sum_i % K
            if sum_i in presum:
                res += presum[sum_i]
            presum[sum_i] = presum.get(sum_i,0) + 1
        return res
        

# @lc code=end

