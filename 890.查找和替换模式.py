'''
Author: Zhou Hao
Date: 2021-05-06 17:15:28
LastEditors: Zhou Hao
LastEditTime: 2021-05-06 17:18:38
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def check(word,pattern):
            if len(word)!=len(pattern):
                return False
            for i in range(len(word)):
                if word.index(word[i])!=pattern.index(pattern[i]):
                    return False
            return True
        res=[]
        for i in range(len(words)):
            if check(words[i],pattern):
                res.append(words[i])
        return res


        
# @lc code=end

