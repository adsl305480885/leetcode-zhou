'''
Author: Zhou Hao
Date: 2021-03-11 17:17:53
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 22:31:37
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=957 lang=python3
#
# [957] N 天后的牢房
#

# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        print(cells)
        circle_result = []

        for day in range(n):  
            if day <= 13:       #14天就是一个循环
                stack = []      #初始化新牢房
                stack.append(0) #首位牢房都是空
                i = 1

                while i>0 and i<7:
                    if cells[i-1] == cells[i+1]:    #左右牢房为空或者都占有
                        stack.append(1)
                    else:
                        stack.append(0)
                    i+=1
                stack.append(0)
                cells = stack       #用当前替换以前的牢房
                print(day,'\t',cells,'\n')
                circle_result.append(cells)
            else:break

        res = (n%14)-1
        result = circle_result[res]
        # print(result)
        return result
# @lc code=end

