'''
Author: Zhou Hao
Date: 2021-04-10 14:48:36
LastEditors: Zhou Hao
LastEditTime: 2021-04-10 19:58:08
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:return 0
        self.res = 0

        def dfs(root):
            if not root:return 0
            
            left = dfs(root.left)
            right= dfs(root.right)

            if root.left:
                left = left +1 if root.left.val == root.val else 0
            if root.right:
                right = right + 1 if root.right.val == root.val else 0
            
            self.res = max(self.res,left+right)
            
            return max(left,right)
            
        dfs(root)
        return self.res 




#[4,4,5,4,4,5]
#[1,null,1,1,1,1,1,1]
# @lc code=end

