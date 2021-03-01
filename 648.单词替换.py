'''
Author: Zhou Hao
Date: 2021-02-28 17:28:34
LastEditors: Zhou Hao
LastEditTime: 2021-02-28 17:45:40
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=648 lang=python3
#
# [648] 单词替换
#

# @lc code=start
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = set(dictionary)

        sentence = sentence.split()
        res = []
        for s in sentence:
            for i in range(len(s)):
                # print(s[:i])
                if s[:i] in root:
                    # print(s[:i],s)
                    s = s[:i]
                    break
            res.append(s)

        # print(sentence)
        # print(" ".join(res))
        return " ".join(res)
# @lc code=end

