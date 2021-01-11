'''
Author: Zhou Hao
Date: 2021-01-11 13:21:39
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 13:53:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    
    '''法一：list -> str -> int -> str -> list'''
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     if sum(digits) == 0:    #判断是否全是0,[0,0,0]
    #         digits[-1] = 1
    #         return digits

    #     digits_str = [str(x) for x in digits]
    #     digits_new = int(''.join(digits_str))
    #     result = digits_new+1
    #     result_list = [int(x) for x in str(result)]
    #     return result_list
        


    '''法二：从后往前依次判断末尾是否为9
       时间 O(n) 
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits       #技巧：前面加0
        for i in range(len(digits)-1,-1,-1):
            #从后向前遍历
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            return digits[1:] 
        else:
            return digits
        
# @lc code=end

