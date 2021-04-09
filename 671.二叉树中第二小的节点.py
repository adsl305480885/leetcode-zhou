'''
Author: Zhou Hao
Date: 2021-04-09 19:42:31
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 20:28:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
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
    # def findSecondMinimumValue(self, root: TreeNode) -> int:
        # cur ,res = [root],[]
        # while cur:
        #     next_lay = []
        #     for node in cur:
        #         res.append(node.val)
        #         if node.left:
        #             next_lay.append(node.left)
        #         if node.right:
        #             next_lay.append(node.right)

        #     cur = next_lay
        
        # if len(set(res)) == 1:return -1
        # for i in sorted(res):
        #     if i!= res[0]:return i 


    '''DFS preorder'''        
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:return -1
        if not root.left and not root.right:
            return -1
        self.min = root.val

        def dfs(root):
            if not root : return -1

            if root.val > self.min:return root.val
            left = dfs(root.left)
            right = dfs(root.right)
            if left < 0: return right
            if right < 0: return left

            return min(left, right)


        return dfs(root)


        
# @lc code=end

