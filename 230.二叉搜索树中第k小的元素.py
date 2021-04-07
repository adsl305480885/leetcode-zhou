'''
Author: Zhou Hao
Date: 2021-04-07 09:41:10
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 10:32:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    '''
        DFS,inorder
        BST 的中序遍历结果是有序的（升序）。
    '''
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
        # res = []
        
        # def dfs(root):
        #     if not root :return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)

        # dfs(root)
        # return res[k-1]


    '''BFS'''
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     cur,res = [root],[]
    #     while cur:
    #         next_lay= []
    #         for node in cur:
    #             if node.left:
    #                 next_lay.append(node.left)
    #             if node.right:
    #                 next_lay.append(node.right)
                    
    #             res.append(node.val)

    #         cur = next_lay
            
    #     res.sort()
    #     return res[k-1]



    '''DFS conut, inorder'''
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        res = []
        self.count = 0      #
        
        def dfs(root):
            if not root:return 
            
            dfs(root.left)
    
            self.count += 1
            if self.count ==k:
                res.append(root.val)
                return

            dfs(root.right)

        dfs(root)

        return res[0]
# @lc code=end

