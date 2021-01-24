'''
Author: Zhou Hao
Date: 2021-01-23 11:08:23
LastEditors: Zhou Hao
LastEditTime: 2021-01-23 11:38:12
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution:
    '''
    方法一：遍历
    '''
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     res = 0
    #     result = []
    #     for n in nums:
    #         if n ==1:
    #             print(res)
    #             res += 1     
    #         elif n == 0 :
    #             result.append(res)
    #             res = 0
            
    #         if n == nums[-1]:
    #             result.append(res)

    #     print(result)
    #     return max(result)



    '''
    方法二:变成字符串，按0切割，然后数最长的
    '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums = [str(x) for x in nums]
        str_nums = ''.join(nums)
        a = str_nums.split('0')
        # print(max(a))

        return len(max(a))   


# @lc code=end

