'''
Author: Zhou Hao
Date: 2021-04-09 22:05:53
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 22:18:54
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    '''BFS'''
    def findMode(self, root: TreeNode) -> List[int]:
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

        from collections import Counter
        count = Counter(res)
        max_time = max(count.values())  
        ans = []
        for k,v in count.items():
            if v == max_time:ans.append(k)

        return ans

            
# @lc code=end

