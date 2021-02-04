'''
Author: Zhou Hao
Date: 2021-01-30 16:11:05
LastEditors: Zhou Hao
LastEditTime: 2021-02-04 17:20:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    
    #方法一：双指针
    # 初始时两个指针分别指向第一个元素位置和最后一个元素的位置。
    # 每次计算两个指针指向的两个元素之和，并和目标值比较。
    # 如果两个元素之和等于目标值，则发现了唯一解。
    # 如果两个元素之和小于目标值，则将左侧指针右移一位。
    # 如果两个元素之和大于目标值，则将右侧指针左移一位。
    # 移动指针之后，重复上述操作，直到找到答案

    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     left,right = 0,len(numbers)-1
    
    #     while  left < right:
    #         temp = numbers[left] + numbers[right]
    #         if temp == target:
    #             return left+1,right+1

    #         elif temp <target:
    #             left +=1
    #         elif temp > target:
    #             right -=1
                

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        n = len(numbers)
        for i in range(n):
            left = i+1
            right = n-1
            while left <= right:
                mid = (left+right)//2
                print(left,right,mid)
                if numbers[i] + numbers[mid] == target:
                    return i+1, mid+1
                elif numbers[i] + numbers[mid] > target:
                    right = mid -1
                elif numbers[i] + numbers[mid] < target:
                    left = mid +1
# @lc code=end

