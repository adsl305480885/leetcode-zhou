import string

'''
Author: Zhou Hao
Date: 2021-01-07 22:38:10
LastEditors: Zhou Hao
LastEditTime: 2021-01-07 23:15:38
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
            方法一：周豪的土方
            1.空字符串直接返回True
            2.先去除字符串中的空格标点，全部转为小写
            3.遍历字符串的下标到长度的一半
                如果长度是奇数，最中间的就不用管，偶数的话正好整除
                判断第i个/倒数第i个是否相等，不相等返回False
                遍历完成，返回True
        '''
        if s == "":return True

        s_new_1 = [x for x in list(s) if x!=' ' and x not in string.punctuation ]
        # print(''.join(s_new_1).lower())
        s_new_2 = ''.join(s_new_1).lower()


        for i in range(len(s_new_2)//2):
            # print(s_new_2[i])
            if s_new_2[i] != s_new_2[len(s_new_2)-i-1]:
                return False

        return True



# @lc code=end

