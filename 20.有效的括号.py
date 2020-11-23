#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    
    def isValid(self, s: str) -> bool:  #返回布尔
        #只判断正确的。太暴力了
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

    
    #栈
    # def isValid(self, s: str) -> bool:

# @lc code=end

