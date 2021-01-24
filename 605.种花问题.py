'''
Author: Zhou Hao
Date: 2021-01-23 09:49:47
LastEditors: Zhou Hao
LastEditTime: 2021-01-23 11:07:54
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        '''贪心算法'''
        flowerbed = flowerbed + [0] #末尾添加哨兵

        i,lenth = 0,len(flowerbed)-1
        res = 0
        while i<lenth:
            if flowerbed[i] == 1:
                i+=2
            elif flowerbed[i+1] == 1:
                i+=3
            else:
                i+=2
                res+=1
        print(res)

        return res >= n
        
        '''dp'''
        # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #     length = len(flowerbed)
        #     flowerbed = [0] + flowerbed + [0]
        #     length += 2
        #     dp = [0]*length
        #     res = 0
        #     for i in range(1, length-1):
        #         if dp[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1] == 0 and flowerbed[i-1]==0:
        #             dp[i] = 1
        #             res+=1
        #     return res >= n


# @lc code=end

