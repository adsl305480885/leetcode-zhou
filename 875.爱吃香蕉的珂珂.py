'''
Author: Zhou Hao
Date: 2021-04-12 16:10:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-12 16:49:37
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] 爱吃香蕉的珂珂
#

# @lc code=start
from typing import List


class Solution:
    def canFinish(self,piles,mid,H)-> bool:
        time = 0
        for p in piles:
            if p <= mid:time +=1
            else:
                time = time + (p // mid) 
                if p%mid:
                    time +=1
        return time <= H


    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:return max(piles)

        left,right = 1,max(piles)
        while left < right:
            # mid = left + ( right-left)//2
            mid = (left + right) //2 
            if self.canFinish(piles,mid,h):right = mid 
            else:left = mid+1

        return left

        
# @lc code=end

