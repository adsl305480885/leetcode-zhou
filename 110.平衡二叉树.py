'''
Author: Zhou Hao
Date: 2021-04-09 21:50:04
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 22:04:00
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    '''DFS'''
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:return True

        def dfs(root):
            if not root:return 0 

            left= dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) >1 or left ==-1 or right == -1:
                return -1
            else:
                return max(left,right)+1

        return dfs(root) != -1

# @lc code=end

