'''
Author: Zhou Hao
Date: 2021-05-06 16:45:40
LastEditors: Zhou Hao
LastEditTime: 2021-05-06 17:06:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1529 lang=python3
#
# [1529] 灯泡开关 IV
#

# @lc code=start
class Solution:
    # 求解的就是统计字符串s中1，0分段有多少段。
    def minFlips(self, target: str) -> int:
        #其实就是奇偶性变来变去，从左至右遍历
        flip_time = 0
        for c in target:
            if flip_time % 2 == 0:
                if c == '1':
                    flip_time += 1
            else:
                if c == '0':
                    flip_time += 1

            # print(c,flip_time)
        return flip_time
        
# @lc code=end

