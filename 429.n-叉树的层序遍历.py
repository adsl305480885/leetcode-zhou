'''
Author: Zhou Hao
Date: 2021-04-06 21:04:31
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 10:22:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:return 

        cur ,res = [root],[]
        while cur:
            next_val , lay_val = [],[]

            for node in cur:
                lay_val.append(node.val)

                for child in node.children:
                    next_val.append(child)

            cur = next_val
            res.append(lay_val)
        
        return res
            
        
# @lc code=end

