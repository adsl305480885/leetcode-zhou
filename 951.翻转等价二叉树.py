'''
Author: Zhou Hao
Date: 2021-04-07 20:48:45
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 21:38:15
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=951 lang=python3
#
# [951] 翻转等价二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    '''DFS'''
    # def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        

    #     def dfs(root1,root2):
    #         if  root1 is root2:return  True
    #         if not root1 or not root2 or root1.val != root2.val:
    #             return False

    #         return (dfs(root1.left, root2.left) and
                # dfs(root1.right, root2.right) or
                # dfs(root1.left, root2.right) and
                # dfs(root1.right, root2.left))
                
                
    #     res = dfs(root1,root2)
    #     return res 
            
            

    '''DFS'''
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        

        def dfs(root1,root2):
            if  root1 is root2:return  True
            if not root1 or not root2 or root1.val != root2.val:
                return False

            left = dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
            right = dfs(root1.left, root2.right) and dfs(root1.right, root2.left)

            return left or right

        return dfs(root1,root2)


# @lc code=end

