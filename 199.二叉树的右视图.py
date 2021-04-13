'''
Author: Zhou Hao
Date: 2021-04-06 19:24:47
LastEditors: Zhou Hao
LastEditTime: 2021-04-11 20:10:13
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
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
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     if not root:return []

    #     cur,res = [root],[]
    #     while cur:
    #         next_lay = []
    #         res.append(cur[-1].val)
    #         for node in cur:
    #             if node.left:next_lay.append(node.left)
    #             if node.right:next_lay.append(node.right)
                
    #         cur = next_lay
    #     return res



    '''DFS'''
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []

        #root -> right -> left
        def dfs(root,deepth):
            if not root :return []

            if deepth == len(res):
                res.append(root.val)
    
            dfs(root.right,deepth+1)
            dfs(root.left,deepth+1)


        dfs(root,0)

        return res

# @lc code=end

