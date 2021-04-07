'''
Author: Zhou Hao
Date: 2021-04-07 19:34:19
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 20:47:27
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=655 lang=python3
#
# [655] 输出二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    '''DFS,preorder'''
    #[1,2,3,4]
    def printTree(self, root: TreeNode) -> List[List[str]]:
        

        def deepth(root):
            if not root:return 0
            
            left = deepth(root.left)
            right = deepth(root.right)
            return max(left,right)+1
        

        deep = deepth(root)
        res = [['' for _ in range(2**deep - 1)] for _ in range(deep)]

        def dfs(root,deepth=0,l=0,r=2**deep-2):
            if not root:return

            mid = (l+r)//2
            res[deepth][mid] = str(root.val)

            dfs(root.left,deepth+1,l,mid-1)
            dfs(root.right,deepth+1,mid+1,r)

        dfs(root)
        return res
        
        
# @lc code=end

