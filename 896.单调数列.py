'''
Author: Zhou Hao
Date: 2021-01-24 12:38:00
LastEditors: Zhou Hao
LastEditTime: 2021-01-24 14:32:23
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    '''方法一:先判断最后一个元素和第一个元素的大小,再遍历
        时间O(n)
    '''
    # def isMonotonic(self, A: List[int]) -> bool:
    #     i = 1
    #     if A[-1] > A[0]:    #增
    #         while i <len(A):
    #             if A[i] < A[i-1]:return False
    #             else:i+=1
    #         return True
            
    #     if A[-1] < A[0]:    #减
    #         while i <len(A):
    #             if A[i] > A[i-1]:return False
    #             else:i+=1
    #         return  True

    #     if A[-1] == A[0]:   #相等
    #         while i<len(A):
    #             if A[i] != A[i-1]:return False
    #             else: i += 1
    #         return  True
    
    
    '''方法二:直接遍历'''
    def isMonotonic(self, A: List[int]) -> bool:
        flag_add = True
        flag_de = True
        
        for i in range(1,len(A)):
            if A[i] < A[i-1]:
                flag_add = False
            if A[i] > A[i-1]:
                flag_de = False
                
        if flag_add==False and flag_de == False:
            return False
        else:return True


        
        
# @lc code=end

