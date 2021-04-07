'''
Author: Zhou Hao
Date: 2021-04-07 11:09:31
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 11:22:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    
    '''DFS,inorder'''
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        def dfs(root):
            if not root:return

            if root.val == val:
                return root          
                
            elif root.val > val:
                return dfs(root.left)
            else:
                return dfs(root.right)

            
        
        return dfs(root)
        
# @lc code=end

