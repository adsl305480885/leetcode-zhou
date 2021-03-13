'''
Author: Zhou Hao
Date: 2021-03-13 15:06:31
LastEditors: Zhou Hao
LastEditTime: 2021-03-13 15:24:11
Description: file conten
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1381 lang=python3
#
# [1381] 设计一个支持增量操作的栈
#

# @lc code=start
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        


    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1


    def increment(self, k: int, val: int) -> None:
        #法一
        # if len(self.stack) <= k:
        #     self.stack = [i+val for i in self.stack]
        # else:
        #     self.stack = [v+val  if i <k else v  for i,v in enumerate(self.stack)]
        
        #法二
        lengh = len(self.stack)
        i = 0
        while i<lengh and  i <k:
            self.stack[i] += val
            i+=1



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
# @lc code=end

