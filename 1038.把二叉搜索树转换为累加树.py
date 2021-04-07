'''
Author: Zhou Hao
Date: 2021-04-07 10:48:51
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 10:49:27
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.sum = 0
        def dfs(root):
            if not root:return 

            dfs(root.right)

            self.sum += root.val
            root.val = self.sum

            dfs(root.left)    


        dfs(root)
        return root
# @lc code=end

