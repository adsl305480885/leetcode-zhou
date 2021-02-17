'''
Author: Zhou Hao
Date: 2021-02-13 14:29:59
LastEditors: Zhou Hao
LastEditTime: 2021-02-13 18:12:18
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#

# @lc code=start
class Solution:

    #寻找乘法因子里面的5的个数
    # def trailingZeroes(self, n: int) -> int:
    #     if  n  < 5:return 0
    #     res = 0
    #     for i in range(1,n+1,1):
    #         if i%5 == 0:
    #             print(i)
    #             while i%5 == 0 :

    #                 res+=1
    #                 i //=5
    #                 print(i,res)

    #     return res
        
    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n >0:
            res += n//5
            n //= 5

        return res
# @lc code=end

