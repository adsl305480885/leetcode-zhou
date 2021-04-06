'''
Author: Zhou Hao
Date: 2021-04-06 16:39:44
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 16:54:35
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''recursion,preorder,DFS'''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(root.val)

        # root_index == 0  # no leftChild
        # root _index == len(preoder) -1  # no rightChild

        if root_index > 0:
            root.left = self.buildTree(inorder[:root_index],postorder[:root_index])
        if root_index != len(inorder)-1:
            root.right = self.buildTree(inorder[root_index+1:],postorder[root_index:-1])

        return root

# @lc code=end

