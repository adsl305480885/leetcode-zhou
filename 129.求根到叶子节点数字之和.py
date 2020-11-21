# @before-stub-for-debug-begin
from python3problem129 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, pre=0):
            if not root: return 0
            cur = pre * 10 + root.val
            print(cur)
            if not root.left and not root.right: return cur
            return helper(root.left, cur) + helper(root.right, cur)
        
        return helper(root)
        


# @lc code=end

