'''
Author: Zhou Hao
Date: 2021-01-12 12:54:40
LastEditors: Zhou Hao
LastEditTime: 2021-01-12 13:11:50
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    
    '''法一：掉包'''
    # def checkRecord(self, s: str) -> bool:
    #     if 'LLL' not in s and s.count('A')<=1:return True
    #     else:return False


    '''法二：遍历'''
    def checkRecord(self, s: str) -> bool:
        if s.find('LLL') != -1:return False
        else:
            count_A = 0
            for i in range(len(s)):
                if s[i] == 'A':
                    count_A+=1
                    if count_A>1:
                        return False

        return True
# @lc code=end

