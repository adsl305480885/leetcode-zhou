'''
Author: Zhou Hao
Date: 2021-03-31 19:58:39
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 20:57:53
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    '''slide windows'''
    def maxVowels(self, s: str, k: int) -> int:

        res = 0
        target = {'a', 'e', 'i', 'o', 'u'}

        i =0
        for j in s[i:i+k]:      #the initial windows
            if j in target:res += 1
        if  res == k :
            return k
        temp = res


        while i < len(s)-k:
            if s[i+k] in target:temp += 1   #the str that add to right
            if s[i] in target :temp -= 1    #the str that decline in left

            if temp == k:return k
            res = max(res,temp)

            i+=1


        return res
# @lc code=end

