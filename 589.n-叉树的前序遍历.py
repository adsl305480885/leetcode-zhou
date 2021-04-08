'''
Author: Zhou Hao
Date: 2021-04-08 10:15:15
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 11:26:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    '''DFS  '''
    # def preorder(self, root: 'Node') -> List[int]:
    #     res = []
        
    #     def dfs(root):
    #         if not root:
    #             return
            
    #         res.append(root.val)
    #         for child in root.children:
    #             dfs(child)
        
    #     dfs(root)
    #     return res

        

    '''迭代'''
    # def preorder(self, root: 'Node') -> List[int]:
        #N叉树前序遍历应该是   根  左->右
        # if not root :return []

        # stack ,res = [root],[]

        # while stack:

        #     node = stack.pop(-1)
        #     res.append(node.val)
            
        #     if node.children:
        #         length = len(stack)
        #         for child in node.children:
        #             stack.insert(length,child)

        # return res
        
        

    '''迭代'''
    def preorder(self, root: 'Node') -> List[int]:
        #N叉树前序遍历应该是   根  左->右
        if not root :return []

        stack ,res = [root],[]

        while stack:

            node = stack.pop(-1)
            res.append(node.val)
            
            stack.extend(node.children[::-1])

        print(res)
        return res
# @lc code=end

