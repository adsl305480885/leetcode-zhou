'''
Author: Zhou Hao
Date: 2021-04-10 14:38:11
LastEditors: Zhou Hao
LastEditTime: 2021-04-10 14:47:54
Description: file content'
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:


    '''DFS preorder'''
    def tree2str(self, t: TreeNode) -> str:
        if not t:return ""
        self.res = ""
        
        def dfs(root):
            if not root :return ''

            self.res += '('+ str(root.val)

            if root.left:
                dfs(root.left)
            elif root.right:
                self.res += '()'
                
            dfs(root.right)
            self.res += ')'
            
        dfs(t)

        return self.res[1:-1]

# @lc code=end

