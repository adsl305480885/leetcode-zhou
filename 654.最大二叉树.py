'''
Author: Zhou Hao
Date: 2021-04-06 15:10:05
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 15:24:30
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    '''recursion,inorder,DFS'''
    '''
        把题目的要求细化，搞清楚根节点应该做什么
        (对于构造二叉树的问题，根节点要做的就是把想办法把自己构造出来)
        然后剩下的事情抛给前/中/后序的遍历框架就行了
    '''
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:return None

        max_val = max(nums)
        max_index = nums.index(max_val)
        
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        
        return root






        

# @lc code=end

