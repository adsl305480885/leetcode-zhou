'''
Author: Zhou Hao
Date: 2021-01-17 17:39:18
LastEditors: Zhou Hao
LastEditTime: 2021-01-18 09:20:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    '''方法一:'''
    # def maxNumberOfBalloons(self, text: str) -> int:
    #     hashmap = {}
    #     for t in text:
    #         if t not in hashmap:
    #             if t == 'l' or t == 'o':hashmap[t] = 0.5
    #             else:
    #                 hashmap[t] = 1
    #         else:
    #             if t == 'l' or t == 'o':
    #                 hashmap[t] += 0.5
    #             else:
    #                 hashmap[t] += 1
                
    #     print(hashmap)
        
    #     new_hashmap = {}
    #     balloon = "balloon"
    #     for b in balloon:
    #         if b in hashmap:
    #             new_hashmap[b] = hashmap[b]
    #         if b not in hashmap:
    #             return 0
    #     print(new_hashmap)        
        
    #     # least_alpha = min(new_hashmap.values()) 
    #     least_alpha = min(new_hashmap, key = new_hashmap.get)
    #     print(least_alpha,new_hashmap[least_alpha])
        
    #     if  new_hashmap['l'] <1 or new_hashmap['o'] <1:
    #         return 0
    #     elif new_hashmap['l'] >=1 and new_hashmap['o'] >=1:
    #         return int(min(new_hashmap.values()))
            
            
    '''方法二:'''
    def maxNumberOfBalloons(self, text: str) -> int:
        import collections


        return min(text.count(key)//num 
        for key,num in collections.Counter('balloon').items())
        
        
        
        
# @lc code=end

