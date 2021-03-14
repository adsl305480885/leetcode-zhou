'''
Author: Zhou Hao
Date: 2021-03-14 20:07:00
LastEditors: Zhou Hao
LastEditTime: 2021-03-14 20:30:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #满二叉树
    # 定义：一个二叉树，如果每一个层的结点数都达到最大值，则这个二叉树就是满二叉树。
    #第n层的节点数量是2^n,根节点算第0层.节点总数是 2^(n+1)-1
 
    '''适合各种二叉树，DFS递归模板'''
    def countNodes(self, root: TreeNode) -> int:
        if not root:return 0 

        #递归查找每个节点的左右子树,DFS
        l = self.countNodes(root.left)
        r = self.countNodes(root.right)
        return l+r+1    #1是这个节点本身
# @lc code=end

