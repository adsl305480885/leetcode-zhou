'''
Author: Zhou Hao
Date: 2021-01-23 23:02:59
LastEditors: Zhou Hao
LastEditTime: 2021-01-24 10:47:17
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    '''
    方法一：暴力法，遍历一次。
    如果元素是0，就把0后面的元素往后依次挪动一位（倒序挪动）
    把0后面一位的元素变成0
    '''
    # def duplicateZeros(self, arr: List[int]) -> None:
    #     """
    #     Do not return anything, modify arr in-place instead.
    #     """
    #     lenth = len(arr)

    #     i=0    
    #     while i<lenth-1:
    #         print(arr[i],i)
    #         if arr[i] == 0:       
    #             #倒序挪动0后面的数组
    #             for j in range(len(arr)-1,i,-1):
    #                 arr[j] = arr[j-1]

    #             arr[i+1] = 0
    #             i+=2
    #         else:i+=1
            


    '''方法二：思路和上面一样'''
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        j = len(arr)
        while i < len(arr):
            if arr[i] == 0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else:i+=1


    '''方法三：双指针快慢指针'''
    
# @lc code=end

