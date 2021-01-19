'''
Author: Zhou Hao
Date: 2021-01-16 22:50:10
LastEditors: Zhou Hao
LastEditTime: 2021-01-18 09:25:00
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        dic = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        lst = list(s)
        
        lst = list(s)
        n = len(s)
        l, r = 0, n - 1

        while l < r:
            if lst[l] in dic and lst[r] in dic:
                print('翻转前:\t',lst[l], lst[r])
                lst[l], lst[r] = lst[r], lst[l]
                print('翻转后:\t',lst[l], lst[r])
                l = l + 1
                r = r - 1
            elif lst[l] not in dic:
                l = l + 1
            elif lst[r] not in dic:
                r = r - 1
    
        return ''.join(lst)

        
        
# @lc code=end

