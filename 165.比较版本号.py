'''
Author: Zhou Hao
Date: 2021-03-31 08:55:56
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 13:05:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        len_1 = len(version1)
        len_2 = len(version2)
        
        if len_1 < len_2:       #get two lists those have the same length
            version1.extend(([0]* (len_2-len_1)))   #use 0 to increase the length of the short list
        elif len_1 > len_2:
            version2.extend(([0]* (len_1-len_2)))


        i = 0
        while i < len(version1):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
            else:
                i+=1

        return 0
# @lc code=end

