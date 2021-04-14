'''
Author: Zhou Hao
Date: 2021-04-14 19:30:47
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 19:40:11
Description: file content

E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
class Solution:
    '''双指针'''
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:return []
        
        m,n = len(firstList),len(secondList)
        i,j = 0,0
        res = []

        while i< m and j < n:
            left_a,right_a = firstList[i]
            left_b,right_b = secondList[j]

            max_left = max(left_a,left_b)
            min_right = min(right_a,right_b)

            if max_left <= min_right:
                res.append([max_left,min_right])

            if right_a < right_b:
                i+=1
            else:j+=1
        return res

# @lc code=end

