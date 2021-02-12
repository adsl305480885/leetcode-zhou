'''
Author: Zhou Hao
Date: 2021-02-12 21:34:53
LastEditors: Zhou Hao
LastEditTime: 2021-02-12 22:21:05
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    
    #暴力字符串方法
    # def reverse(self, x: int) -> int:
        
    #     # -2147483648~2147483648
    #     if x >=0:
    #         if int(str(x)[::-1]) > 2147483647:return 0 
    #         return int(str(x)[::-1])
    #     else:
    #         if int('-'+(str(x)[-1:0:-1])) < -2147483648:
    #             return 0 
    #         # print(int('-'+(str(x)[-1:0:-1])))
    #         return int('-'+(str(x)[-1:0:-1]))
            


    def reverse(self, x: int) -> int:
        if x >= 0 :flag = True
        else:flag = False
        
        y = abs(x)
        # print(len(x))
        res = 0
        while y != 0:
            res = res*10+y%10
            y = y//10
            print(y,res)
            
        res = res if flag else -res
        return res if -2147483648<res<2147483647 else 0



        
# @lc code=end

