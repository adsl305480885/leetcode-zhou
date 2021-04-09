'''
Author: Zhou Hao
Date: 2021-04-09 17:10:47
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 19:05:49
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
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
    # def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # if not root1 and not root2:return None
        # if not root1:return root2
        # if not root2:return root1
        

        # def dfs(root1,root2):
        #     if not root1 and not root2:return None
        #     if not root1:return root2
        #     if not root2:return root1

        #     root = TreeNode(root1.val+root2.val)

        #     root.left=dfs(root1.left,root2.left)
        #     root.right = dfs(root1.right,root2.right)

        #     return root
            
        # return  dfs(root1,root2)
        


    '''BFS'''
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return None
            
        if not root1:return root2
        if not root2:return root1
        
        cur = [(root1,root2)]
        while cur:
            node1,node2 = cur.pop()
            node1.val += node2.val

            if node1.left and node2.left:
                cur.append((node1.left,node2.left))
            elif not node1.left and node2.left:
                node1.left = node2.left

            if node2.right and node1.right:
                cur.append((node1.right,node2.right))
            elif not node1.right and node2.right:
                node1.right = node2.right

        return root1

# @lc code=end

