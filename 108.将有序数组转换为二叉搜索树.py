#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    '''DFS inorder'''
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def dfs(nums):
            if not nums:return

            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = dfs(nums[0:mid])
            root.right = dfs(nums[mid+1:])

            return root

        return dfs(nums)




# @lc code=end

