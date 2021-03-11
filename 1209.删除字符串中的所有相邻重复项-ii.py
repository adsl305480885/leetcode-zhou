'''
Author: Zhou Hao
Date: 2021-03-10 21:36:34
LastEditors: Zhou Hao
LastEditTime: 2021-03-10 21:55:31
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if not stack or stack[-1][0] != i:
                stack.append([i,1])

            elif stack[-1][1]<k-1:
                stack[-1][1] += 1
            else:
                stack.pop()



            # if  len(stack) >=k and  len(set(stack[-k:])) == 1:
            #     del stack[-k:]




        # print(stack)
        res =''.join([ i[0]*i[1] for i in stack])
        # print(res)
        return res
# @lc code=end

