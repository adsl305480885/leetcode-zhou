'''
Author: Zhou Hao
Date: 2021-04-07 08:51:53
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 09:40:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=652 lang=python3
#
# [652] 寻找重复的子树
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
    
    '''DFS,postorder'''
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        hashmap = {}    #记录其他节点的子树
        
        def dfs(root):
            if not root:return '#'

            left_sub = dfs(root.left)
            right_sub = dfs(root.right)


            sub = left_sub + ',' + right_sub +',' + str(root.val)
            if sub in hashmap:
                hashmap[sub] += 1
            else:
                hashmap[sub] = 1
                
            if hashmap[sub] == 2:res.append(root)

            return sub


        dfs(root)
        return res


# @lc code=end

