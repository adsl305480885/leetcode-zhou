'''
Author: Zhou Hao
Date: 2021-03-09 19:32:13
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 20:01:26
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            stack.append(a)

            while len(stack)>=2 and stack[-1] <0 and stack[-2] >0:  #右－ 左 + 才会相撞
                    temp = stack[-1] + stack[-2]
                    if temp >0: #左边大
                        stack.pop()
                    elif temp ==0:  #两个星星一样大
                        stack.pop()
                        stack.pop()
                    elif temp <0:   #右边大
                        del stack[-2]


        # print(stack)
        return stack
# @lc code=end

