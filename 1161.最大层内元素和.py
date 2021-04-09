'''
Author: Zhou Hao
Date: 2021-04-08 22:35:52
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 23:06:43
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
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
    # def maxLevelSum(self, root: TreeNode) -> int:
    #     if not root.left and not root.right:return 1

    #     cur ,res = [root],[]

    #     while cur:
    #         next_lay ,lay_val = [], []

    #         for node in cur:
    #             lay_val.append(node.val)
    #             if node.left:
    #                 next_lay.append(node.left)
    #             if node.right:
    #                 next_lay.append(node.right)

    #         cur= next_lay
    #         res.append(lay_val)

    #     # print(res)

    #     sum_ = [sum(r) for r in res]
    #     # print(sum_)

    #     return sum_.index(max(sum_))+1
        

    '''DFS inorder'''
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import defaultdict
        
        def inorder(node, level):
            if node:
                inorder(node.left, level + 1)

                if level not in  level_sum:
                    level_sum[level] = node.val
                else:
                    level_sum[level] += node.val

                inorder(node.right, level + 1)
            

        level_sum = defaultdict(int)
        inorder(root, 1)
    
        max_ = max(level_sum.values())

        list1= sorted(level_sum.items(),key=lambda x:x[0])  #对键进行排序
        
        for i,j in list1:
            if j == max_:return i


# @lc code=end

