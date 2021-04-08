'''
Author: Zhou Hao
Date: 2021-03-31 08:49:10
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 16:00:28
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:return 0
        self.ans = float('-inf')

        def dfs(root):
            if not root:return 0
            
            left = max(0,dfs(root.left))
            right = max(0,dfs(root.right))
            self.ans = max(self.ans,left+right+root.val)
            return max(left,right) + root.val
            
        dfs(root)
        return self.ans
# @lc code=end

