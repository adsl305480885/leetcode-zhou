'''
Author: Zhou Hao
Date: 2021-04-27 10:27:54
LastEditors: Zhou Hao
LastEditTime: 2021-04-27 11:51:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start


class Solution:
    '''
    动态规划三要素:  重叠子问题，最优子结构，状态方程
    
    思维框架: 明确状态  ->  定义dp数组/函数的定义  ->  明确选择  ->  明确base case
    要符合最优子结构，子问题之间必须相互独立
    '''
    

    '''动态规划 递归'''
    # def coinChange(self, coins: List[int], amount: int) -> int:
        
        # memo = dict()       #备忘录字典，避免重复子问题
        # def dp(n:amount):
            
        #     #base case
        #     if n == 0 :return 0
        #     if n <0 : return -1

        #     if n in memo:return memo[n] #查备忘录
        #     res = float('inf')      #初始化为无穷大
        #     for coin in coins:
        #         subproblem = dp(n-coin) #递归得到每个硬币的最优解
        #         if subproblem <0 :continue  #无解就跳过,剪枝
        #         res = min(res,1+subproblem)
        #     memo[n] = res if res != float('inf') else -1
        #     return memo[n]
            
        # return dp(amount)



    '''动态规划，迭代,自底向上'''
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount+1] * (amount+1)        #base case
        dp[0] = 0

        for i in range(amount+1):
            for coin in coins:
                if i - coin <0 :continue
                dp[i] = min(dp[i], 1+dp[i-coin])        #状态转移方程

        return dp[amount] if dp[amount] != amount + 1 else -1



    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     dp = [0] + [10001] * amount     #base case

    #     for coin in coins:
    #         for j in range(coin, amount + 1):
    #             dp[j] = min(dp[j], dp[j - coin] + 1)        #状态转移方程
    #     return dp[-1] if dp[-1] != 10001 else -1

# @lc code=end

