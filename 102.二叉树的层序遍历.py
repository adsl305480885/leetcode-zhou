'''
Author: Zhou Hao
Date: 2021-03-09 20:32:41
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 21:04:40
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #层序遍历就是广度优先,每一层从左遍历到右,再遍历下一层
        
        #迭代
        if not root:
            return []
        cur ,res = [root],[]
        while cur:
            lay,lay_val = [],[] #每一层的节点和值
            
            for node in cur:#迭代当前层的节点
                lay_val.append(node.val)
                
                #获取当所有当前层节点的所有子节点(所有下一层节点)
                if node.left:lay.append(node.left)
                if node.right:lay.append(node.right)
            cur = lay
            res.append(lay_val)
        return res


        


# @lc code=end

