'''
Author: Zhou Hao
Date: 2021-04-06 15:31:50
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 16:54:43
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        
        # root_index == 0  # no leftChild
        # root _index == len(preoder) -1  # no rightChild

        if root_index >0 :
            root.left = self.buildTree (preorder[1:1+root_index],inorder[:root_index])
        if root_index != len(preorder) -1:
            root.right = self.buildTree(preorder[root_index+1:],inorder[root_index+1:])
        

        
        return root
        


# @lc code=end

