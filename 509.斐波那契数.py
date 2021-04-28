'''
Author: Zhou Hao
Date: 2021-01-28 21:40:45
LastEditors: Zhou Hao
LastEditTime: 2021-04-27 10:27:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    #递归
    # def fib(self, n: int) -> int:
    #     if n == 0 :return 0
    #     if n == 1:  return 1
        
    #     res = self.fib(n-1) + self.fib(n-2)
    #     return res
        

    # '''动态规划'''
    # def fib(self, n: int) -> int:
    #     if n==0:return 0
    #     if n==1 or n==2:return 1

    #     dp = [0] * (n+1)
    #     dp[0] = 0
    #     dp[1] = dp[2] = 1

    #     for i in range(3,n+1):
    #         dp[i] = dp[i-1]+dp[i-2]
    #     return dp[n]



    '''优化空间后的动态规划'''
    def fib(self, n: int) -> int:
        if n==0:return 0
        if n==1 or n==2:return 1

        pre,cur = 1,1
        for i in range(3,n+1):
            sum = pre+cur
            pre = cur 
            cur = sum
            
        return cur
# @lc code=end