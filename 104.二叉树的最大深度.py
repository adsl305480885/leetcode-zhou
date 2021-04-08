'''
Author: Zhou Hao
Date: 2021-04-08 12:47:14
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 13:17:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root:return 0

    #     cur,res = [root] ,0

    #     while cur:
    #         res+=1
    #         next_lay = []
    #         for node in cur:
    #             if node.left:
    #                 next_lay.append(node.left)
    #             if node.right:
    #                 next_lay.append(node.right)

    #         cur = next_lay
        
    #     return res
        


    '''DFS'''
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0

        def dfs(root):
            if not root:return 0
            elif not root.left and not root.right:return 1
            else:
                max_deep = []
                if root.left:
                    max_deep.append(dfs(root.left))
                if root.right:
                    max_deep.append(dfs(root.right))
                
                return max(max_deep)+1

        return dfs(root)

# @lc code=end

