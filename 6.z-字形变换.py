'''
Author: Zhou Hao
Date: 2021-03-31 13:58:17
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 17:05:10
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    # def convert(self, s: str, numRows: int) -> str:
    #     if numRows == 1:return s
        
    #     a = []
    #     flag = True     #判断这列是否有numrows个, True menas not have
    #     temp = 0
        
    #     # 把每列合成一个字符串
    #     for i in range(len(s)):
    #         if not a:
    #             a.append(s[i])
    #             continue

    #         if len(a[-1]) < numRows and flag:
    #             a[-1] += s[i]
                
    #             if len(a[-1]) == numRows:
    #                 flag = False        #False means has
    #                 temp = i  

    #         else:
    #             if i - temp <= numRows-2:
    #                 if len(a[-1]) == numRows:
    #                     a.append(s[i])
    #                 else:
    #                     a[-1] = s[i] + a[-1]

    #             elif i-temp == numRows-1:
    #                 flag = True
    #                 a.append(s[i])


    #     if len(a) == 1:
    #         return a[0]

    #     #长度不够的用0填充
    #     for i in range(len(a)-1):
    #             if len(a[i]) < numRows:
    #                 a[i] = '0' + a[i] + '0'

    #     #处理最后一列
    #     if flag:
    #         a[-1] = a[-1]+'0'*(numRows-len(a[-1]))
    #     else:
    #         a[-1] = '0'*(numRows - len(a[-1]) -1)+a[-1]+'0'


    #     res = ''
    #     for n in range(numRows):
    #         for i in range(len(a)):
    #             res += a[i][n]  if a[i][n] != '0' else ''
                

    #     return res


    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c     # 把每个字符 c 填入对应行 
            if i == 0 or i == numRows - 1: 
                flag = -flag    #在达到 Z 字形转折点时，执行反向
            i += flag   #更新当前字符 c 对应的行索引；
        return "".join(res)
# @lc code=end

