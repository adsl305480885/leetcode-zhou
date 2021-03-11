'''
Author: Zhou Hao
Date: 2021-03-11 09:46:23
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 12:12:27
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
class Solution:
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     stack = []
    #     pop,push =0,0

    #     while pop < len(popped) :

    #         if push < len(pushed):
    #             stack.append(pushed[push])
    #             push += 1

    #         print(stack,popped[pop])

    #         while stack and stack[-1] == popped[pop]:
    #             stack.pop()
    #             if pop <len(popped)-1:
    #                 pop+=1
    #             print(stack,popped[pop],'******')

    #         if push == len(pushed) and not stack:
    #             return True

    #         if push == len(pushed) and stack[-1] != popped[pop]:
    #             return False
                
    #     return True
        


    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #用栈来模拟
        stack = []
        pop = 0
        for i in pushed:
            stack.append(i)
            # print(stack,popped[pop])
            while stack and stack[-1] == popped[pop]:
                # print(stack,popped[pop])
                stack.pop()
                # print(stack,'*****')
                pop += 1

            # print(stack,'\n')
        return not stack

    
# @lc code=end

