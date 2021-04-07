# @before-stub-for-debug-begin
# from python3problem701 import *
# from typing import *
# @before-stub-for-debug-end

'''
Author: Zhou Hao
Date: 2021-04-07 11:23:36
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 13:49:25
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    
    '''DFS'''
    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #     if not root:return TreeNode(val)

    #     if val < root.val:
    #         root.left = self.insertIntoBST(root.left,val)
    #     else:
    #         root.right = self.insertIntoBST(root.right,val)

    #     return root


    '''DFS'''
    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    #     if not root:return TreeNode(val)

    #     def dfs(root,val):
    #         if not root:return TreeNode(val)
            

    #         if val > root.val:
    #             if root.right:
    #                 dfs(root.right,val)
    #             else:
    #                 root.right = TreeNode(val)
    #         else:
    #             if root.left:
    #                 dfs(root.left,val)
    #             else:
    #                 root.left = TreeNode(val)

    #     dfs(root,val)
        
    #     return root
        


    '''DFS'''
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:return TreeNode(val)
        
        def dfs(root,val):
            if not root:
                return TreeNode(val)


            if val > root.val:
                root.right = dfs(root.right,val)
            else:
                root.left = dfs(root.left,val)
                
            return root
        
        dfs(root,val)

        return root

# @lc code=end

