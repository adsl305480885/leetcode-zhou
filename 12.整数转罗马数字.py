'''
Author: Zhou Hao
Date: 2021-03-30 21:32:45
LastEditors: Zhou Hao
LastEditTime: 2021-03-30 23:00:54
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start
class Solution:
    
    '''method 1: violence'''
    # def intToRoman(self, num: int) -> str:
        
    #     hashmap = {
    #         1:'I',
    #         5:'V',
    #         10:'X',
    #         50:'L',
    #         100:'C',
    #         500:'D',
    #         1000:'M',

    #         4:'IV',
    #         9:'IX',
    #         40:'XL',
    #         90:'XC',
    #         400:'CD',
    #         900:'CM',
    #     }

    #     res = ''
    #     i = 1

    #     while num >0:
    #         i *= 10
    #         temp = num %10 * i //10
    #         num //= 10


    #         if temp in hashmap:
    #             res = hashmap[temp] + res
    #         else:
    #             temp_res = ''
    #             while temp >0:
    #                 if temp >= (i//2):
    #                     temp %= (i//2)
    #                     temp_res = hashmap[(i//2)] 
    #                 else:
    #                     temp -= i//10
    #                     temp_res = temp_res+ hashmap[i//10] 


    #             res = temp_res +res

    #     return res



    '''method 2: greedy'''
    def intToRoman(self, num: int) -> str:
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        res = ''
        for key in hashmap:  # greedy, from big to small,from left to right
            if num // key != 0:
                times = num // key
                res += hashmap[key] * times
                num %= key

        # print(res)
        return res

# @lc code=end

