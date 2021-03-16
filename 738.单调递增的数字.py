'''
Author: Zhou Hao
Date: 2021-03-16 21:01:04
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 22:07:32
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=738 lang=python3
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution:
    #从后往前遍历，如果发现后面的比前面小，前面的-1，后面的全部置9
    def monotoneIncreasingDigits(self, N: int) -> int:
        N = [int(i) for i in  str(N)]
        de_N = N[::-1]
        for i in range(len(de_N)-1):
            if de_N[i] < de_N[i+1]:
                de_N[i+1] = de_N[i+1] -1    #前面-1
                for j in range(i+1):        #后面全部9
                    de_N[j] = 9

        res = 0
        for i in range(len(de_N)):
            res += de_N[i] * pow(10,i)
        return res
        
# @lc code=end

