'''
Author: Zhou Hao
Date: 2021-01-11 21:19:57
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 21:38:28
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    
    '''法一：哈希字典'''
    def letterCombinations(self, digits: str) -> List[str]:
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return [] 
        product=['']
        for k in digits:
            product=[i+j for i in product for j in conversion[k]]
            print(product)
        return product
        



        
        
# @lc code=end

