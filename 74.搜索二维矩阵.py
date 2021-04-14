'''
Author: Zhou Hao
Date: 2021-04-13 22:05:42
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 09:20:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
from typing import List


class Solution:
    '''二分:根据索引二分'''
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     def binay_search(lists,target):
    #         left,right = 0,len(lists)-1
    #         while left <=right:
    #             mid = (left+right) //2
    #             if lists[mid] == target:return True
    #             elif lists[mid] < target:left = mid +1
    #             elif lists[mid]>target:right = mid-1

    #         return False
            
    #     for i in matrix:        #在每一行中二分，节省时间
    #         if i[-1]==target or i[0]==target:
    #             return True
    #         elif i[-1] > target:
    #             if binay_search(i,target):
    #                 return True
    #             else:continue
    #         elif i[-1] < target:
    #             continue
    #     return False

    

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:return True
            else:continue
        return False
    
        
# @lc code=end

