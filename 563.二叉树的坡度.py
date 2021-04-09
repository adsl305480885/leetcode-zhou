'''
Author: Zhou Hao
Date: 2021-04-09 16:44:31
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 17:09:29
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
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
    # def findTilt(self, root: TreeNode) -> int:
    #     if not root:return 0
    #     if not root.left and not root.right:return 0

    #     res = []
    #     self.sum_ = 0
    #     def dfs(root):
    #         if not root :return 0

    #         left = dfs(root.left)
    #         right = dfs(root.right)
    #         res.append(abs(left-right))

    #         self.sum_ = left+right+root.val
    #         return self.sum_

    #     dfs(root)
 
    #     return sum(res)



   




# @lc code=end

