'''
Author: Zhou Hao
Date: 2021-04-09 16:05:21
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 16:40:38
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''DFS preorder'''
    # def sumOfLeftLeaves(self, root: TreeNode) -> int:
    #     if not root:return 0
    #     if not root.left and not root.right:return 0

    #     res = []
    #     def dfs(root):
    #         if not root:return

    #         if root.left and not root.left.left and not root.left.right:
    #             res.append(root.left.val)

    #         dfs(root.left,)
    #         dfs(root.right)
            

    #     dfs(root)
    #     return sum(res)


    '''BFS'''
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0
        if not root.left and not root.right:return 0

        cur = [root]
        res = 0
        while cur:
            next_val = []
            for node in cur:
                if node.left:
                    next_val.append(node.left)
                    if not node.left.left and not node.left.right:
                        res+= node.left.val
                if node.right:
                    next_val.append(node.right)

            cur = next_val
        return res


#[1,2,3,4,5]
#[1,null,2]
# @lc code=end

