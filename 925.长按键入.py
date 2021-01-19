'''
Author: Zhou Hao
Date: 2021-01-18 00:00:17
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 00:41:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    '''双指针'''
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:return True
        name,typed = list(name),list(typed)
        
        if name[0] != typed[0]:return False
        if name[-1] != typed[-1]:return False


        
        n ,t = 0,0
        while t < len(typed):
            print(n,t,'-----------------')
            if name[n] == typed[t]: #匹配name中的字符
                print('aaaaa',name[n],typed[t])
                if n < len(name)-1: 
                    n+=1
                t+=1
                print('aaaaa',n,t)
            else:
                if typed[t] == typed[t-1]:  #长键输入
                    print('bbbb',name[n],typed[t])
                    t+=1
                    print('bbbb',n,t)
                else:
                    return False
                
        print(n,t)
        if n == len(name)-1:
            return True
        else:return False
        
# @lc code=end

