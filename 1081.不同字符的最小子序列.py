'''
Author: Zhou Hao
Date: 2021-03-13 15:53:26
LastEditors: Zhou Hao
LastEditTime: 2021-03-13 21:03:16
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
    #利用栈。
    # 三个要求：
    # 去重
    # 字母之间顺序不被打乱
    # 返回字典序最小的结果：例如"bcabc"可能有两种结果bca和abc，返回abc。
    # 栈可以直接满足前两个要求。
    # 对第三个要求，字母入栈前先判断栈顶元素是否在后面出现过，如果栈顶元素在后面还出现过并且大于当前元素，则将栈顶元素出栈。
        if not s:
            return ""
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue    #避免重复添加

            #保留字典序最小的字符，删除字典序较大的字符
            while stack and c < stack[-1] and stack[-1] in s[i+1:]:
                stack.pop()
            stack.append(c)
        return "".join(stack)
# @lc code=end

