'''
Author: Zhou Hao
Date: 2021-04-08 10:26:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 10:55:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    '''DFS'''
    # def postorder(self, root: 'Node') -> List[int]:
    #     res = []

    #     def dfs(root):
    #         if not root :return 

    #         for child in root.children:
    #             dfs(child)

    #         res.append(root.val)   
        
    #     dfs(root)
    #     return res


    '''迭代'''
    def postorder(self, root: 'Node') -> List[int]:
        if not root:return []

        stack ,res = [root],[]
        while stack:
            node = stack.pop()      #子结点 从右结点开始出栈
            res.append(node.val)
            for child in node.children:
                stack.append(child)     #子结点  从左子结点开始入栈

        #循环结束后res里面是  根 右->左  的顺序
        #N叉树后续遍历应该是  左->右 根
        return res[::-1]


    
# @lc code=end

