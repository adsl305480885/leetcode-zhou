'''
Author: Zhou Hao
Date: 2021-04-08 12:24:12
LastEditors: Zhou Hao
LastEditTime: 2021-05-07 11:13:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
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
    # def minDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0

    #     cur,res = [root],0
    #     while cur:
    #         res +=1
    #         next_lay = []
    #         for node in cur:
    #             if node.left:
    #                 next_lay.append(node.left)
    #             if node.right:
    #                 next_lay.append(node.right)

    #             if not node.left and not node.right:
    #                 return res
    #         cur = next_lay



    '''DFS,preorder'''
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0
        

        def dfs(root):
            if not root:return 0

            elif not root.left and not root.right:  return 1

            else:
                child_deepth = []
                if root.left:
                    child_deepth.append(dfs(root.left))
                if root.right:
                    child_deepth.append(dfs(root.right))
                return min(child_deepth)+1




        return dfs(root)


# @lc code=end

