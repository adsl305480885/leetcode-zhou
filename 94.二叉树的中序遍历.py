'''
Author: Zhou Hao
Date: 2021-03-09 16:02:42
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 16:30:41
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #      递归基础模板
    #     if not root:return []
        
    #前序递归
    #     return \
    #         self.inorderTraversal(root.left) \
    #         + [root.val] \
    #         + self.inorderTraversal(root.right)
    
    # 中序递归 
    # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    # # 后序递归
    # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        #递归通用模板,可以根据情况改参数
        def dfs(cur):
            #深度优先遍历(前中后)
            if not cur:
                return      
            # 前序递归
            # res.append(cur.val)
            # dfs(cur.left)
            # dfs(cur.right) 
            
            # 中序递归
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)

            # # 后序递归
            # dfs(cur.left)
            # dfs(cur.right)
            # res.append(cur.val)      
        res = []
        dfs(root)
        return res
            


# @lc code=end

