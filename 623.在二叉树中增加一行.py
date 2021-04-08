'''
Author: Zhou Hao
Date: 2021-04-08 16:03:00
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 21:46:38
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
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
    # def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
    #     if not root:return None

    #     if depth == 1:
    #         new_root = TreeNode(val)
    #         new_root.left = root
    #         return new_root

    #     if depth == 2:
    #         new_left = TreeNode(val)
    #         new_right = TreeNode(val)
            
    #         new_left.left = root.left
    #         new_right.right = root.right
            
    #         root.left = new_left
    #         root.right = new_right
    #         return root
            
    #     self.addOneRow(root.left,val,depth-1)
    #     self.addOneRow(root.right,val,depth-1)

    #     return root



    '''DFS'''
    # def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
    #     if not root :return None

    #     def dfs(root,depth,val):
    #         if not root :return None
            
    #         if depth == 1:
    #             new = TreeNode(val)
    #             new.left = root
    #             return new

    #         if depth == 2:
    #             new_left = TreeNode(val)
    #             new_right = TreeNode(val)
                
    #             new_left.left  = root.left
    #             new_right.right = root.right

    #             root.left = new_left
    #             root.right = new_right
    #             return root
    #         else:
    #             dfs(root.left,depth-1,val)
    #             dfs(root.right,depth-1,val)
    #             return root
                    
    #     return dfs(root,depth,val)
        


    '''BFS'''
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            if depth == d-1:    # 找到第d-1层
                break
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)   
        for node in queue:
            L = TreeNode(v)
            R = TreeNode(v)
            L.left = node.left
            R.right = node.right
            node.left = L
            node.right = R
        return root



# @lc code=end

