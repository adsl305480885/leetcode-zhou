'''
Author: Zhou Hao
Date: 2021-03-16 14:16:31
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 15:09:34
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    '''贪心'''
    # 如果连续上涨，就等价于每天买入卖出，比较昨天和今天
    #下降就不买，单日上涨也买
    #综上，遍历价格表，比较今天和昨天的加个。如果比昨天高就买昨天的，今天卖
    # def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i,p in enumerate(prices):
        #     if i == 0 :
        #         continue
            
        #     if prices[i] > prices[i-1]: #比昨天高就买昨天的，今天卖
        #         res += prices[i] - prices[i-1]
        

        # return res
        

    '''单增栈，比较今天和昨天的加价格'''
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0

        for p in prices:
            if not stack:stack.append(p)
            
            else:
                if p < stack[-1]:   #降价
                    stack.clear()
                    stack.append(p)
                elif p >stack[-1]:      #涨价，如果连续上涨，就等价于每天买入卖出
                    res += p-stack[-1]
                    stack.append(p)

        return res
# @lc code=end

