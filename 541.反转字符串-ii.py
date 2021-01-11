'''
Author: Zhou Hao
Date: 2021-01-11 20:30:14
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 21:19:00
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    
    '''方法一：不使用list，纯str翻转
        时间复杂度高
    '''
    # def reverseStr(self, s: str, k: int) -> str:
        # if len(s) < k :
        #     return s[::-1]      #如果少于k个，则逆序输出

        # elif k<=len(s)<2*k:
        #     a = s[:k][::-1]
        #     b = s[k:]
        #     # print(a,'\t',b,'\t',a+b)
        #     return a+b
        
    
        # for i in range(0,len(s)-1,2*k):

        #     # if i 
        #     head = s[i:i+k][::-1]
        #     tail = s[i+k:i+2*k]
        #     # print(i,'\t',head,'\t',tail)
        #     s = s[0:i]+head+tail+s[i+2*k:]
            
        #     # print(s)
            
        # return s


    '''方法二：list翻转,滑动窗口，窗口大小为2k, O(n/k)'''
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0,len(a),2*k):
            a[i:i+k] = a[i:i+k][::-1] 
        return "".join(a)

        

        
# @lc code=end

