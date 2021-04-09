'''
Author: Zhou Hao
Date: 2021-04-09 20:58:21
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 21:37:49
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
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
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        
    #     def dfs(p,q):
    #         if not p and not q:return True
    #         if not p:return False
    #         if not q:return False
            
    #         if p.val != q.val :return False
    #         else:
    #             left = dfs(p.left,q.left)
    #             right = dfs(p.right,q.right)
    #             return left and right 
            
    #     return dfs(p,q)


    '''BFS'''        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:return True
        if not p:return False
        if not q:return False
        if p.val != q.val:return False


        cur = [(p,q)]
        while cur:
            node1,node2 = cur.pop()
            if node1.val != node2.val:return False
            

            if node1.left and node2.left:
                cur.append((node1.left,node2.left))
            elif (node1.left and not node2.left) or (not node1.left and node2.left):
                return False

            if node1.right and node2.right:
                cur.append((node1.right,node2.right))
            elif (node1.right and not node2.right) or (not node1.right and node2.right):
                return False


        return True
    

#[1,2] \n [1,null,2]
# @lc code=end

