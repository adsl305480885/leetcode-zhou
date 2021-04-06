'''
Author: Zhou Hao
Date: 2021-04-06 21:10:56
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 22:20:42
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:

    '''BFS'''
    # def largestValues(self, root: TreeNode) -> List[int]:
    #     if not root:return []
    #     cur,res = [root],[]

    #     while cur:
    #         next_lay = []
    #         tem_max = float('-inf')
    #         for node in cur:
    #             if node.left:next_lay.append(node.left)
    #             if node.right:next_lay.append(node.right)
    #             tem_max = max(tem_max,node.val)

    #         cur = next_lay
    #         res.append(tem_max)

    #     return res
        

    # def largestValues(self, root: TreeNode) -> List[int]:
    #     if not root:return []
    #     cur,res = [root],[]

    #     while cur:
    #         next_lay = []
    #         lay_val = []
    #         for node in cur:
    #             if node.left:next_lay.append(node.left)
    #             if node.right:next_lay.append(node.right)
    #             lay_val.append(node.val)

    #         cur = next_lay
    #         res.append(max(lay_val))
            

    #     return res


    #[3,1,5,0,2,4,6]
    #[1,3,2,5,3,null,9]
    '''DFS   looks like 199.二叉树的右试图'''
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:return []
        res = [] 
        
        #root -> left -> right
        def dfs(root,deepth):
            if not root :return 

            if len(res) == deepth:
                res.append(root.val)
            else:
                res[deepth] = max(res[deepth], root.val)
            

            dfs(root.left,deepth+1)
            dfs(root.right,deepth+1)

        dfs(root,0)
        return res


# @lc code=end