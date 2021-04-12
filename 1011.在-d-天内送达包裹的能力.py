'''
Author: Zhou Hao
Date: 2021-04-12 16:54:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-12 19:04:35
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] 在 D 天内送达包裹的能力
#

# @lc code=start
from typing import List


class Solution:
    
    
    '''二分查找寻找作边界'''
    def canFinish(self,weights,mid ,D):
        day = 1
        temp =0
        for w in weights:
            if temp +w <= mid:
                temp += w    
            else:
                day += 1
                temp = w
        return day <=D


    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left ,right = max(weights),sum(weights)
        while left <right:
            mid = left + (right-left)//2
            if self.canFinish(weights,mid ,D):right = mid
            else:left = mid+1
        return left
        
# @lc code=end

