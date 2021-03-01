'''
Author: Zhou Hao
Date: 2021-03-01 21:15:14
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 21:33:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=554 lang=python3
#
# [554] 砖墙
#

# @lc code=start
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        hashmap = {}
        length = [len(x) for x in wall]
        if sum(length) == len(wall):return len(wall)
        
        #找出每一行的边界
        for row in wall:
            temp = 0
            for cloumn in row[:-1]:
                temp += cloumn
                #边界当作键，边界的次数当作值
                hashmap[temp] = hashmap.get(temp,0) + 1
        return len(wall) - max(hashmap.values())
# @lc code=end

