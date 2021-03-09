'''
Author: Zhou Hao
Date: 2021-03-09 21:06:37
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 21:24:58
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        #在层序遍历的基础上加一个标记用来翻转
        if not root:
            return []
        cur ,res,flag = [root],[],False
        while cur:
            lay,lay_val = [],[] #每一层的节点和值
            
            for node in cur:#迭代当前层的节点
                lay_val.append(node.val)
                
                #获取当所有当前层节点的所有子节点(所有下一层节点)
                # if flag:
                if node.left:lay.append(node.left)
                if node.right:lay.append(node.right)
                    # flag = False
                # else:
                #     if node.right:lay.append(node.right)
                #     if node.left:lay.append(node.left)
                #     flag = True
            flag = bool(1-flag)
                
            cur = lay
            if flag:
                res.append(lay_val)
            else:res.append(lay_val[::-1])
        return res
# @lc code=end

