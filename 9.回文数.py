'''
Author: Zhou Hao
Date: 2021-01-11 15:07:44
LastEditors: Zhou Hao
LastEditTime: 2021-01-11 15:35:35
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    '''方法一'''
    # def isPalindrome(self, x: int) -> bool:
    #     str_x = str(x)
    #     for i in range(0,len(str_x)//2,1):
    #         if str_x[i] == str_x[len(str_x)-i-1]:pass
    #         else:return False

    #     return True
        
    '''方法二'''
    # def isPalindrome(self, x: int) -> bool:
    #     return True if str(x) == str(x)[::-1] else False
        

    '''方法三：进阶，不用str()
        x//10取余数，遍历，一位一位地逆序存入一个列表[个，十，百，千，万...]
        再对比
    '''
    def isPalindrome(self, x: int) -> bool:
        if x < 0:return False
        elif x < 10: return True
        x_copy = x

        num_list = []       #[个，十，百，千，万......]
        while x_copy >0:
            num_list.append(x_copy%10)     #从个位开始逆序存入列表
            x_copy = x_copy // 10 

    
        index = len(num_list)-1
        while  x>0:
            # print( x%10,'\t',num_list[index])
            if x%10 == num_list[index]:
                #
                print( x%10,'\t',num_list[index])
                x = x//10
                index-=1
            else:
                return False
        return True

            


        
# @lc code=end

