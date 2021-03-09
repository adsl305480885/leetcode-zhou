'''
Author: Zhou Hao
Date: 2020-12-19 18:37:42
LastEditors: Zhou Hao
LastEditTime: 2021-03-07 14:20:56
Description: file conten
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
import math
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min_stack = [math.inf]     #辅助栈,保存每次push后的最小值

    def push(self, x: int) -> None:
        self.items.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.items.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

