'''
Author: Zhou Hao
Date: 2021-02-24 17:35:47
LastEditors: Zhou Hao
LastEditTime: 2021-02-24 19:38:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#

# @lc code=start
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter

        res = None
        for i in A:
            c = Counter(i)      #字典
            if res == None:
                res = c
            res &= c            #求交集
        # print(res.elements())
        return res.elements()
        
# @lc code=end

