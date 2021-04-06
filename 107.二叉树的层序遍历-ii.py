'''
Author: Zhou Hao
Date: 2021-04-06 20:05:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 20:17:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''BFS'''
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res = []
        cur = [root]

        while cur:
            next_lay = []
            lay_value = []
            for node in cur:
                lay_value.append(node.val)
                if node.left:next_lay.append(node.left)
                if node.right:next_lay.append(node.right)
            cur = next_lay
            res.append(lay_value)

        return res[::-1]
        
# @lc code=end

