'''
Author: Zhou Hao
Date: 2021-04-06 11:37:24
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 11:59:01
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    二叉树题目的一个难点就是，如何把题目的要求细化成每个节点需要做的事情。
    写递归算法的关键是要明确函数的「定义」是什么，然后相信这个定义，利用这个定义推导最终结果，绝不要跳入递归的细节。


'''

class Solution:
    '''recursion,preorder'''
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root == None:return None
        
    #     root.left,root.right = root.right,root.left
    #     self.invertTree(root.left)      #recursion
    #     self.invertTree(root.right)
        
    #     return root
    

    '''recursion,postorder'''
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:return None
        
        self.invertTree(root.left)      #recursion
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left

        return root
# @lc code=end

