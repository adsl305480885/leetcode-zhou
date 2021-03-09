'''
Author: Zhou Hao
Date: 2021-03-09 16:36:10
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 16:38:43
Description: file contentt
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []

        # return \
        #     self.postorderTraversal(root.left) \
        #     + self.postorderTraversal(root.right) \
        #     + [root.val]
            

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root :return
            
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)


        res = []
        dfs(root)
        return res
# @lc code=end

