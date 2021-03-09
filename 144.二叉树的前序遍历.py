'''
Author: Zhou Hao
Date: 2021-03-09 16:32:49
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 16:35:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    #     if not root:
    #         return []

    #     return \
    #         [root.val] \
    #         + self.preorderTraversal(root.left) \
    #         + self.preorderTraversal(root.right)
            

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root :
                return 
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
        res = []
        dfs(root)
        return res
        
# @lc code=end

