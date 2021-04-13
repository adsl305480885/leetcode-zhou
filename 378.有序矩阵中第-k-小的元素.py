'''
Author: Zhou Hao
Date: 2021-04-13 21:00:15
LastEditors: Zhou Hao
LastEditTime: 2021-04-13 22:29:29
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#

# @lc code=start
from typing import List


class Solution:

    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
    #     num = 0
    #     lists = []
    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[i])):
    #             lists.append(matrix[i][j])

    #     for l in sorted(lists):
    #         num += 1
    #         if num == k:
    #             return l


    '''二分'''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left,right = matrix[0][0],matrix[-1][-1]    #根据值来二分

        while left <right:
            mid = (left+right) //2

            smaller_nums = 0
            for i in matrix:
                for j in i:
                    if j <=mid:         #注意闭区间
                        smaller_nums += 1

            if smaller_nums <k:        #注意闭区间
                left =mid+1     #在右边
            else:
                right = mid

        return left
        
# @lc code=end

