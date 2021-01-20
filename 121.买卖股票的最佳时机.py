'''
Author: Zhou Hao
Date: 2021-01-20 16:40:35
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 22:12:17
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    '''错误方法！！！！！滑动窗口:超时'''
    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) == 1:return 0

    #     money = {}
    #     for i in range(len(prices)-1):
    #         max_prices = max(prices[i+1:])
    #         if prices[i] >= max_prices:
    #             money[i+1] = 0
    #         elif prices[i] < max_prices:
    #             money[i+1] = max_prices - prices[i]

    #     print(money)
    #     return max(money.values())

    '''错误方法二:倒序pop,超时'''
    # def maxProfit(self, prices: List[int]) -> int:
    #     if len(prices) == 1:return 0
    #     best = 0

    #     for i in range(len(prices)-1,0,-1):    #倒序遍历
    #         min_price = min(prices[:i])
    #         if min_price < prices[i]:                
    #             if prices[i] - min_price > best:
    #                 best = prices[i] - min_price
    #             prices.pop(i)
                
    #     return best
        

    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')     #正无穷
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit


# @lc code=end

