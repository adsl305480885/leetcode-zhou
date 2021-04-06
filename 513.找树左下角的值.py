'''
Author: Zhou Hao
Date: 2021-04-06 20:17:55
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 21:03:34
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
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
    # def findBottomLeftValue(self, root: TreeNode) -> int:
        # res,cur = [],[root]
        # while cur:
        #     next_lay,lay_val = [],[]
        #     for node in cur:
        #         lay_val.append(node.val)
        #         if node.left:
        #             next_lay.append(node.left)
        #         if node.right:
        #             next_lay.append(node.right)

        #     cur = next_lay
        #     res.append(lay_val)

        # return res[-1][0]
        

    '''DFS'''
    def findBottomLeftValue(self, root: TreeNode) -> int:



        res = [root.val,0]

        #root -> left-> right
        def dfs(root,deepth):
            if not root :return []
            
            if res[-1] < deepth:
                res[0] = root.val
                res[-1] +=1
    
            dfs(root.left,deepth+1)
            dfs(root.right,deepth+1)


        dfs(root,0,)

        return res[0]

# @lc code=end

