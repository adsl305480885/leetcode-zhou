'''
Author: Zhou Hao
Date: 2021-04-08 13:17:44
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 15:31:26
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if not root:return True

    #     cur,res = [root],[]
    #     while cur:
    #         next_val,lay_val = [],[]

    #         for node in cur:
    #             if node:
    #                 lay_val.append(node.val)
    #                 next_val.append(node.left)
    #                 next_val.append(node.right)
    #             else:
    #                 lay_val.append('#')
                    
    #         cur = next_val
    #         res.append(lay_val)
    

    #     for r in res[1:]:   #第一层肯定对称
    #         length_r = len(r)
    #         if length_r %2 != 0:    #如果这层有奇数个，肯定不对称
    #             return False
            
    #         if r[:length_r//2] != r[length_r//2:][::-1]:
    #             return False

    #     return True


    '''DFS'''
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:return True


        def dfs(node1,node2):
            if not node1 and not node2:return True
            if not node1 or not node2:return False
            
            else:
                return node1.val == node2.val \
                    and dfs(node1.left,node2.right)\
                    and dfs(node1.right,node2.left)

        return dfs(root.left,root.right)

# @lc code=end

