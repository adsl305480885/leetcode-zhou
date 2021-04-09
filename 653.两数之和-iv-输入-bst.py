'''
Author: Zhou Hao
Date: 2021-04-09 20:30:42
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 20:57:34
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
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
    # def findTarget(self, root: TreeNode, k: int) -> bool:
        # if not root:return False
        # if not root.left and not root.right:return False

        # cur,res = [root],[]
        # while cur:
        #     next_lay = []
        #     for node in cur:
        #         res.append(node.val)
        #         if node.left:
        #             next_lay.append(node.left)
        #         if node.right:
        #             next_lay.append(node.right)

        #     cur = next_lay    

        # for r in res:
        #     if k-r in res:
        #         if k-r == r and res.count(r) >1:
        #             return True
        #         elif k-r!=r:
        #             return True

        # return False



    '''DFS'''
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:return False
        if not root.left and not root.right:return False

        res = []
        def dfs(root):
            if not root:return 

            dfs(root.left)
            res.append(root.val)
            dfs(root.right)

        dfs(root)

        #double pointers
        i,j = 0,len(res)-1
        while i <j:
            if res[i] + res[j] == k:
                return True
            elif res[i] + res[j] > k:
                j-=1
            else :
                i+=1
        return False
# @lc code=end

