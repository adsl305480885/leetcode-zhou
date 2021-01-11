'''
Author: Zhou Hao
Date: 2021-01-11 14:32:35
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 15:03:36
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    
    '''法一:掉包str.count()'''
    # def firstUniqChar(self, s: str) -> int:
    #     for index,value in enumerate(s.lower()):
    #         times = s.count(value)
    #         if  times == 1:     #遇到第一个只出现一次的就输出
    #             return index
    
    #     return -1


    
    '''法二:哈希字典'''
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}

        for index,value in enumerate(s.lower()):
            if not hashmap.get(value):
                hashmap[value] = 1
            else:
                hashmap[value] += 1
                
        for k,v in hashmap.items():
            if v == 1:
                return s.index(k)
                
        return -1
                
        
        


        
# @lc code=end

