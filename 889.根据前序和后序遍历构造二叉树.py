'''
Author: Zhou Hao
Date: 2021-04-06 16:52:37
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 19:23:41
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #[3,9,20,15,7] \n [9,15,7,20,3]
    #   [2,1] \n  [1,2]
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not (pre or post): return None

        root = TreeNode(pre[0])

        if len(pre) > 1  :
            root_index = post.index(pre[1])

            root.left = self.constructFromPrePost(pre[1:2+root_index],post[:root_index+1])
            root.right = self.constructFromPrePost(pre[2+root_index:],post[root_index+1:-1])

        return root
# @lc code=end

