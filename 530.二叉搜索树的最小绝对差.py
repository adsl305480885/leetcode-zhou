'''
Author: Zhou Hao
Date: 2021-04-10 14:15:56
LastEditors: Zhou Hao
LastEditTime: 2021-04-10 14:17:02
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    '''bFS'''
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        cur,res = [root],[]
        while cur:
            next_lay = []
            for node in cur:
                res.append(node.val)
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)
                cur = next_lay

        res.sort()
 
        ans = float('inf')
        for i in range(1,len(res)):
            ans = min(ans,abs(res[i]-res[i-1]))

        return ans
        

    '''DFS,inorder'''
    # def getMinimumDifference(self, root: TreeNode) -> int:
    #     self.res= float('inf')
        
    #     ans = []

    #     def dfs(root):
    #         if not root:return float('inf')
                
    #         dfs(root.left)
    #         ans.append(root.val)      
    #         dfs(root.right)


    #     dfs(root)
    #     print(ans)


    #     res = float('inf')
    #     for i in range(1,len(ans)):
    #         res = min(res,abs(ans[i]-ans[i-1]))

    #     return res
        
# @lc code=end

