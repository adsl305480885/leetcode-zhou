'''
Author: Zhou Hao
Date: 2021-04-06 22:21:24
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 08:49:29
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    '''looks like 515,199'''

    '''BFS'''
    # def deepestLeavesSum(self, root: TreeNode) -> int:
        # cur,res = [root],[]
        # while cur:
        #     next_lay , lay_val = [],[]

        #     for node in cur:
        #         if node.left:
        #             next_lay.append(node.left)
        #         if node.right:
        #             next_lay.append(node.right)

        #         lay_val.append(node.val)
        #     cur = next_lay
        #     res.append(lay_val)

        
        # return sum(res[-1])
        


    '''DFS'''
    # def deepestLeavesSum(self, root: TreeNode) -> int:
        # self.ans = 0
        # self.maxdepth = 0
        
        # def dfs(depth, node):
        #     if not node:return 
            
        #     if node.left or node.right:
        #         dfs(depth + 1, node.left)
        #         dfs(depth + 1, node.right)
        
        #     else:
        #         if depth > self.maxdepth:
        #             self.maxdepth = depth
        #             self.ans = node.val
        #         elif depth == self.maxdepth:
        #             self.ans += node.val

        # dfs(0, root)
        # return self.ans


    



# @lc code=end

