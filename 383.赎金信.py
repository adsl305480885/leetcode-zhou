'''
Author: Zhou Hao
Date: 2021-04-22 16:22:35
LastEditors: Zhou Hao
LastEditTime: 2021-04-22 16:26:19
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        count = Counter(magazine)

        for i in ransomNote:
            if i in count:
                if count[i] >=1:
                    count[i] -= 1
                else:
                    return False
            else:
                return False
                

        return True
# @lc code=end

