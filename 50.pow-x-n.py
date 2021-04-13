'''
Author: Zhou Hao
Date: 2021-04-13 21:44:40
LastEditors: Zhou Hao
LastEditTime: 2021-04-13 22:04:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:

    '''二分，分治'''
    def myPow(self, x: float, n: int) -> float:
        
        def two_pow(x,n):
            if n==0:return 1    #分治递归结束条件
            if n== 1:return x

            res = two_pow(x,n//2)       #递归
            if n %2 ==0:            #分治汇总,判断奇偶
                return res*res
            else:return res*res*x

        if n<0:return 1/two_pow(x,-n)
        return two_pow(x,n)
        
# @lc code=end

