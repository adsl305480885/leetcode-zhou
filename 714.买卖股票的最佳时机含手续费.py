'''
Author: Zhou Hao
Date: 2021-03-17 09:53:09
LastEditors: Zhou Hao
LastEditTime: 2021-03-17 17:16:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        buy = prices[0]

        for i in range(1,len(prices)):
            if prices[i] < buy:
                buy = prices[i]                 
            elif prices[i] - fee > buy:
                res += prices[i]-buy-fee
                buy = prices[i]-fee     #亮点
        return res
# @lc code=end

