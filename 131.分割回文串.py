'''
Author: Zhou Hao
Date: 2021-04-26 17:17:08
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 22:03:32
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    

    # def partition(self, s: str) -> List[List[str]]:
        
    #     self.isPalindrome = lambda s : s == s[::-1]
    #     res = []
    #     self.backtrack(s, res, [])
    #     return res
            
    # def backtrack(self, s, res, path):
    #     if not s:
    #         res.append(path)
    #         return
    #     for i in range(1, len(s) + 1): #注意起始和结束位置
    #         if self.isPalindrome(s[:i]):
    #             self.backtrack(s[i:], res, path + [s[:i]])



    '''回溯模板'''
    def partition(self, s: str) -> List[List[str]]:
        
        def dfs(s):
            if len(s) == 0:
                res.append(track[:])
                # return
            
            for j in range(len(s)):
                if s[:j+1] != s[:j+1][::-1]:    #判断是不是回文
                    continue        #剪枝
                
                track.append(s[:j+1])
                dfs(s[j+1:])
                track.pop()


        res ,track = [],[]
        dfs(s)
        return res


# @lc code=end

