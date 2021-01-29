'''
Author: Zhou Hao
Date: 2021-01-28 17:23:23
LastEditors: Zhou Hao
LastEditTime: 2021-01-28 21:16:22
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    
    #方法一:奇偶分开再遍历合并
    # def sortArrayByParityII(self, A: List[int]) -> List[int]:
    #     x_ = [x for x in A if x%2 ==0]  #偶
    #     y_ = [y for y in A if y%2 !=0]  #奇
        
    #     res = []
    #     for  i in range(len(A)):
    #         if i %2 ==0:
    #             res.append(x_[0])
    #             x_.remove(x_[0])
    #         else:
    #             res.append(y_[0])
    #             y_.remove(y_[0])

    #     return res
        
        
    #不分开遍历一次
    # def sortArrayByParityII(self, A: List[int]) -> List[int]:
    
    #     res = len(A)*[0] #创建指定长度，指定初始元素的列表
    #     i = 0   #偶
    #     j = 1   #奇
    #     for _ in A:
    #         if _ %2 ==0:
    #             res[i] = _
    #             i+=2
    #         else:
    #             res[j] = _
    #             j+=2


    #     return res
        
    #双指针         奇偶指针
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        i = 0   #偶指针
        j = 1   #奇指针

        while i<len(A) and j<len(A):
            if A[i] %2 ==0:
                i+=2
            if A[j] %2 !=0:
                j+=2
            # if A[i]%2 !=0 and A[j] %2 ==0:
            # print(i,j,A[i],A[j])
            if  i < len(A) and j < len(A):
                print(i,j,A[i],A[j])
                A[i],A[j] = A[j],A[i]

        return A


# @lc code=end

