'''
Author: Zhou Hao
Date: 2021-04-09 14:13:34
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 15:10:59
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    '''DFS inorder'''
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:return []
        hashmap = {}

        def dfs(root):
            if not root :return 0

            left = dfs(root.left)
            right = dfs(root.right)
            total = left + right +root.val
            hashmap[total] = hashmap.get(total,0)+1
            return  total

        dfs(root)
        
        max_ = max(hashmap.values())
        res = [k for k,v in hashmap.items() if v== max_]

        return  res
# @lc code=end

