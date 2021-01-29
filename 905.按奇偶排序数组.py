'''
Author: Zhou Hao
Date: 2021-01-28 16:48:46
LastEditors: Zhou Hao
LastEditTime: 2021-01-28 17:23:10
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#

# @lc code=start
class Solution:
    
    '''方法一:双指针'''
    # def sortArrayByParity(self, A: List[int]) -> List[int]:
    #     i,j =0,len(A)-1
    #     while i<j:
    #         if A[i] %2 !=0 and A[j] %2 ==0: #前奇后偶
    #             A[i],A[j] = A[j],A[i]
    #             i+=1
    #             j-=1
    #         elif A[i] %2 !=0 and A[j] %2 !=0:  #前奇后奇
    #             j-=1
    #         elif A[i] %2 ==0 and A[j] %2 !=0:  #前偶后奇
    #             i+=1
    #             j-=1
    #         elif A[i] %2 ==0 and A[j] %2 ==0:  #前偶后偶
    #             i+=1
                
    #     return A
        

    #分别找到奇偶，再合并.
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x%2==0]+[y for y in A if y%2 !=0]
# @lc code=end

