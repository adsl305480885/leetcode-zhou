'''
Author: Zhou Hao
Date: 2021-04-09 22:25:08
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 22:51:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    '''bFS'''
    def minDiffInBST(self, root: TreeNode) -> int:
        
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
        

    '''DFS'''

#[71,62,84,14,null,null,88]
# @lc code=end

