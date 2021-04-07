'''
Author: Zhou Hao
Date: 2021-04-07 10:57:25
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 11:07:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:

    '''DFS,preorder'''
    def isValidBST(self, root: TreeNode) -> bool:

        def dfs(root,min,max):
            if not root:return True


            if min and (root.val <= min.val):return False
            if max and (root.val >= max.val):return False

            return dfs(root.left,min,root) and dfs(root.right,root,max)


        
        return dfs(root,None,None)
        
# @lc code=end

