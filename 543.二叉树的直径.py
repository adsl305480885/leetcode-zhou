'''
Author: Zhou Hao
Date: 2021-04-10 14:18:20
LastEditors: Zhou Hao
LastEditTime: 2021-04-10 14:35:12
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''DFS postorder'''
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(root):
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(left+right+1,self.res)

            return max(left ,right ) + 1

        dfs(root)

        return self.res -1

# @lc code=end

