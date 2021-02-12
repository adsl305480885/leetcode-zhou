'''
Author: Zhou Hao
Date: 2021-02-08 20:23:57
LastEditors: Zhou Hao
LastEditTime: 2021-02-09 20:46:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    #method 1: baoli
    # def arrangeCoins(self, n: int) -> int:
    #     i = 1
    #     while i<=n:
    #         n=n-i
    #         i = i+1
    #         # print(n,i)
    #     return i -1



    #method 2: binnar-search
    # 1.二分查找，设立左右边界分别为0和n，每次取中间值mid为行数，将mid行总数和n对比
    # 2.和n相等时直接return mid，小于n时，左边界left=mid+1 ，大于n时，右边界right = mid-1
    # 3.在不断的判定后如果硬币不能刚好分完，那么left会等于能分的最多行数+1，right会等于总量超出n的最小行数-1，即为能分的最多行数，return right

    def arrangeCoins(self, n: int) -> int:
        left,right = 0,n
        while left<=right:
            mid = (left+right)//2   
            count = (1+mid)*mid/2
            if count ==n:return mid
            elif count < n :
                left = mid + 1
            elif count > n :right = mid -1
        return right


# @lc code=end

