'''
Author: Zhou Hao
Date: 2021-03-10 22:04:06
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 09:41:48
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=636 lang=python3
#
# [636] 函数的独占时间
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] *n
        #单线程CPU，所有函数都是栈内运行，递归

        for l in logs:
            logs_list = l.split(':')
            if logs_list[1] == 'start':     #发现start就入栈
                stack.append([logs_list[0],logs_list[2]])      #[id,time]

            else:       #发现end就出栈,每个end结束的都是当前栈顶函数
                temp = int(logs_list[2]) - int(stack[-1][1]) + 1     #计算栈顶函数运行时间
                res[int(stack[-1][0])]  += temp
                stack.pop() #栈顶函数（当前结束函数出栈）

                if stack:       #栈顶非空，下一个出栈的函数-当前函数时间
                    res[int(stack[-1][0])] -= temp
        return res
# @lc code=end

