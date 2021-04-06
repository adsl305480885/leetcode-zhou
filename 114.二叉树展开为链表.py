'''
Author: Zhou Hao
Date: 2021-03-31 08:49:10
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 15:05:42
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''recursion,postorder,DFS'''
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root or (not root.left and not root.right):
            return root
        
        #先把左右子树捋直，递归
        self.flatten(root.left)
        self.flatten(root.right)
        
        tmp = root.right #把捋直的右子树备份一下
        
        root.right = root.left #把捋直的左子树放到右边
        root.left = None #记得把左子树置空
        while(root.right): #找到现在右子树的最后一个node
            root = root.right
        root.right = tmp #把捋直的原来的右子树接上去



        
# @lc code=end

