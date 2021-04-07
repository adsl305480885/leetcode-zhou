'''
Author: Zhou Hao
Date: 2021-04-07 13:01:47
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 13:35:37
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#[0] \n 0
class Solution:
    

    '''DFS'''
    # def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
    #     def getMIn(root:TreeNode):
    #         # look for the most small node in the right child
    #         while root.left:
    #             root = root.left

    #         return root
        

    #     def dfs(root,key):
    #         if not root:return  None

    #         if root.val == key:
    #             if not root.left :return root.right
    #             if not root.right : return root.left

    #             min = getMIn(root.right) 
    #             root.val = min.val
    #             root.right = dfs(root.right,min.val)
            
    #         elif root.val < key:
    #             root.right = dfs(root.right,key)
    #         elif key < root.val:
    #             root.left =  dfs(root.left,key)

    #         return root

    #     root = dfs(root,key)
    #     return root



    '''DFS'''
    def getMin(self,node):
        while node.left:node = node.left
        return node

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:return None
        
        if root.val == key:
            if not root.left:return root.right
            if not root.right:return root.left
            
            min_rightChild = self.getMin(root.right)
            root.val = min_rightChild.val
            root.right = self.deleteNode(root.right,min_rightChild.val)

        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            root.left = self.deleteNode(root.left,key)

        return root
        


# @lc code=end

