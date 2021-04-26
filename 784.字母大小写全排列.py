'''
Author: Zhou Hao
Date: 2021-04-26 22:43:47
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 22:53:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:

    def letterCasePermutation(self, S: str) -> List[str]:
        ans=[]
        def helper(s,pre):
            if not s:
                ans.append("".join(pre))
                return
            if s[0].isalpha():
                helper(s[1:],pre+[s[0].upper()])
                helper(s[1:],pre+[s[0].lower()])
            else:
                 helper(s[1:],pre+[s[0]])
        helper(S,[])
        return ans
        
# @lc code=end

