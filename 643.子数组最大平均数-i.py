'''
Author: Zhou Hao
Date: 2021-01-24 16:58:58
LastEditors: Zhou Hao
LastEditTime: 2021-01-24 17:41:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        '''滑动窗口,向右滑动一位，右边加左边减'''
        '''滑动窗口,向右滑动一位，右边加左边减'''
        sum_flag = sum(nums[:k])
        print(sum_flag)
        res = sum_flag

        for i in range(k,len(nums)):
            sum_flag = sum_flag+nums[i]-nums[i-k]
            res = max(res,sum_flag)
            print('sum_flag:',sum_flag,'\tsum_k:',res,i)
        print(res/k)
        return res/k
# @lc code=end

