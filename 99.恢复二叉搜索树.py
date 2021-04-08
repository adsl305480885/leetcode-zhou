'''
Author: Zhou Hao
Date: 2021-04-08 09:40:16
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 10:12:28
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #TODO
    '''DFS inorder'''
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

        def dfs(root):
            if not root:return
                
            dfs(root.left)

            if self.firstNode == None and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            
            dfs(root.right)

        dfs(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val

# @lc code=end

