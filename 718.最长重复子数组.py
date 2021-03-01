'''
Author: Zhou Hao
Date: 2021-03-01 11:24:03
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 14:01:28
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#

# @lc code=start
class Solution:
    #滑动窗口
    def findLength(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)

        if m>n:
            m, n, A, B = n, m, B, A

        tmp_list = []
        result = 0

        str_B = ',' + ','.join([str(i) for i in B]) + ','

        for r in A:
            tmp_list.append(str(r))

            if ',' + ','.join(tmp_list) + ',' in str_B:
                result = max(result, len(tmp_list))

            else:
                tmp_list = tmp_list[1:] #滑

        return result
# @lc code=end

