'''
Author: Zhou Hao
Date: 2021-01-17 23:30:19
LastEditors: Zhou Hao
LastEditTime: 2021-01-17 23:54:27
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
class Solution:
    '''方法一：'''
    # def destCity(self, paths: List[List[str]]) -> str:
    #     from_city , to_city = [],[]
    #     for p in paths:
    #         from_city.append(p[0])
    #         to_city.append(p[1])
    #     for f in from_city:
    #         if f in to_city:to_city.remove(f)

    #     return to_city[0]
        
        
    '''方法二：hash'''
    def destCity(self, paths: List[List[str]]) -> str:
        hashmap ={}

        for p in paths:
            hashmap[p[0]] = p[1]
        print(hashmap)

        for k,v in hashmap.items():
            if v not in hashmap:
                print(v)
                return v

# @lc code=end

