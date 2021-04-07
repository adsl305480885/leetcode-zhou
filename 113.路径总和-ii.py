'''
Author: Zhou Hao
Date: 2021-04-07 18:35:17
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 19:32:26
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    '''DFS'''
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
    #     res = []
    #     self.dfs(root, sum, res, [])
    #     return res

    # def dfs(self, root, sum, res, path):
    #     if not root: # 空节点，不做处理
    #         return
    #     if not root.left and not root.right: # 叶子节点
    #         if sum == root.val: # 剩余的「路径和」恰好等于叶子节点值
    #             res.append(path + [root.val]) # 把该路径放入结果中
                
    #     self.dfs(root.left, sum - root.val, res, path + [root.val]) # 左子树
    #     self.dfs(root.right, sum - root.val, res, path + [root.val]) # 右子树

        


    '''DFS'''
    # def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        
    #     def dfs(root,sum,path):
    #         '''importance:  need use path +    but not path.append() '''

    #         if not root:return 

    #         if not root.left and not root.right:    #leaf node
    #             if sum == root.val:
    #                 res.append(path +[root.val])

    #         dfs(root.left, sum - root.val,  path + [root.val]) # 左子树
    #         dfs(root.right, sum - root.val,  path + [root.val]) # 右子树

    #     res =[]
    #     path = []
    #     dfs(root,sum,path)
    #     return res

        

    '''BFS'''
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == targetSum:
                res.append(tmp)
                
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res


# @lc code=end

