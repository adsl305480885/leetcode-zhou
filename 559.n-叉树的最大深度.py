'''
Author: Zhou Hao
Date: 2021-04-08 11:27:39
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 12:44:31
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
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
    '''BFS'''
    # def maxDepth(self, root: 'Node') -> int:
    #     if not root :return 0

    #     cur  = [root]
    #     num = 0
        
    #     while cur:
    #         next_lay = [] 
    #         num +=1 

    #         for node in cur:
    #             for child in node.children:
    #                 next_lay.append(child)
    #         cur = next_lay

    #     return num

        
    '''DFS, preorder'''
    def maxDepth(self, root: 'Node') -> int:

        def dfs(root):
            if not root:return 0
            
            if not root.children:return 1
            else:
                child_deepth = []
                for child in root.children:
                    child_deepth.append(dfs(child))
                    
                return max(child_deepth)+1

        res = dfs(root)
        return res




# @lc code=end

