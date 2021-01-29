'''
Author: Zhou Hao
Date: 2021-01-28 21:40:45
LastEditors: Zhou Hao
LastEditTime: 2021-01-28 21:46:53
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
    def fib(self, n: int) -> int:
        if n == 0 :return 0
        if n == 1:  return 1
        
        res = self.fib(n-1) + self.fib(n-2)
        return res
# @lc code=end

