'''
Author: Zhou Hao
Date: 2021-02-23 13:06:17
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 13:22:43
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    '''hashtabl'''
    # def findWords(self, words: List[str]) -> List[str]:
    #     first = "qwertyuiop"
    #     second = "asdfghjkl"
    #     third = "zxcvbnm"

    #     res = []

    #     for w in words:
    #         hashmap = {}
    #         for i in w:
    #             if i in first:
    #                 hashmap[1] = i
    #             if i in second:
    #                 hashmap[2] = i
    #             if i in third:
    #                 hashmap[3] = i
                
    #             if len(hashmap) >1:continue
    #         if len(hashmap) == 1:res.append(w)

    #     # print(res)
    #     return res


    '''set'''
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        res = []
        for w in words:
            setw = set(w.lower())
            if setw <= set1 or setw <= set2 or setw <= set3:
                res.append(w)
        return res
# @lc code=end

