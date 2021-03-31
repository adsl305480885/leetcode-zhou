'''
Author: Zhou Hao
Date: 2021-03-31 17:06:23
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 18:45:38
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=609 lang=python3
#
# [609] 在系统中查找重复文件
#

# @lc code=start
class Solution:
    
    '''method-1:hash'''
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hashmap = {}


        for p in paths:

            file = p.split(' ')
            for content in file[1:]:
                temp = content.index('(')

                if content[temp:] not in hashmap:
                    hashmap[content[temp:]] = [file[0]+'/'+content[:temp]]
                else:
                    hashmap[content[temp:]].append(file[0]+'/'+content[:temp])


        res = []
        for v in hashmap.values():    
            if len(v) > 1:
                res.append(v) 
        return res
# @lc code=end

