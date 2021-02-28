'''
Author: Zhou Hao
Date: 2021-02-28 23:11:24
LastEditors: Zhou Hao
LastEditTime: 2021-02-28 23:26:01
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            hashmap = {}
            for j in range(len(points)):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                distance = x*x + y*y
                if distance not in hashmap:
                    hashmap[distance] = 1
                else:
                    hashmap[distance] += 1
            # print(hashmap)
            for v in hashmap.values():
                if v >1:
                    res += v*(v-1)      #数学公式，排列
                    
        # print(res)
        return res
# @lc code=end

