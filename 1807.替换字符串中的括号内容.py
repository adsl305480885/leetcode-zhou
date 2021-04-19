'''
Author: Zhou Hao
Date: 2021-04-19 20:39:41
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 21:24:17
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1807 lang=python3
#
# [1807] 替换字符串中的括号内容
#
import re
# @lc code=start
class Solution:


    def evaluate(self, s, knowledge):
        # 转换knowl为字典
        paras = {i[0]: i[1] for i in knowledge}
        stack = []
        ret = ''
        # 创建转换标识符
        change = False
        for i in s:
            # 当左括号将标识符设置为True
            if i == '(':
                change = True
            elif i == ')':
                # 当遇到右括号，重置标识符与stack并开始判断knowledge
                change = False
                ret += paras.get(''.join(stack), '?')
                stack = []
            else:
                # change为False追加字符串，为True时append栈等待获取key
                if change:
                    stack.append(i)
                else:
                    ret += i
        return ret
            
# @lc code=end

