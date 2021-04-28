'''
Author: Zhou Hao
Date: 2021-04-26 23:06:56
LastEditors: Zhou Hao
LastEditTime: 2021-04-27 09:19:08
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1286 lang=python3
#
# [1286] 字母组合迭代器
#

# @lc code=start
class CombinationIterator:

    '''回溯,参考77.组合，不看顺序，状态变量是begin'''
    def __init__(self, characters: str, combinationLength: int):
        global track 
        track = ""

        def dfs(start):
            global track 
            if len(track) >= combinationLength:
                self.res.append(track[:])
                return

            for i in range(start,len(characters)):
                track += characters[i]
                dfs(i+1)
                track= track[:-1]

        self.res = []
        dfs(0)

    def next(self) -> str:
        if self.res:
            return  self.res.pop(0)

    def hasNext(self) -> bool:
        return self.res != []

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

