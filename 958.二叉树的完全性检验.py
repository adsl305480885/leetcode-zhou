'''
Author: Zhou Hao
Date: 2021-04-08 21:22:06
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 09:15:42
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=958 lang=python3
#
# [958] 二叉树的完全性检验
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
#     def isCompleteTree(self, root: TreeNode) -> bool:
#         if not root :return True
#         if not root.left and not root.right :return True

#         cur,res = [root],[]

#         while cur:
#             next_val , lay_val= [],[]
#             for node in cur:
#                 if node:
#                     lay_val.append(node.val)
#                     next_val.append(node.left)
#                     next_val.append(node.right)
#                 else:
#                     lay_val.append('#')

#             cur = next_val
#             res.append(lay_val)
#         print(res)
# 5
#         if len(set(res[-1])) == 1:res.pop()
        
#         if len(res) >2:
#             for r in res[:-1]:
#                 if r.count('#') !=0:
#                     return False
        
#         null = res[-1].count('#')
#         for v in res[-1][::-1][:null] :
#             if v == '#': 
#                 null -= 1
                
#         return null == 0
            

        
        





# @lc code=end
#[1,null,2]
#[1,2]
#[1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]

