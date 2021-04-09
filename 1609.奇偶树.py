'''
Author: Zhou Hao
Date: 2021-04-09 19:06:07
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 19:31:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1609 lang=python3
#
# [1609] 奇偶树
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
    # def isEvenOddTree(self, root: TreeNode) -> bool:
    #     if root.val %2 ==0:
    #         return False

    #     jishu,oushu,cur = [],[],[root]
    #     flag = True
    #     while cur:
    #         next_val,lay_val, = [],[]
    #         for node in cur:
    #             lay_val.append(node.val)
    #             if node.left:
    #                 next_val.append(node.left)
    #             if node.right:
    #                 next_val.append(node.right)

    #         cur = next_val
    #         if flag:
    #             oushu.append(lay_val)
    #         else:
    #             jishu.append(lay_val)
    #         flag = bool(1-flag)


    #     for o in oushu:
    #         if o[0] %2==0:return False
    #         for i in range(1,len(o)):
    #             if o[i]%2==0:return False
    #             if o[i] <= o[i-1]:return False
                
    #     for j in jishu:
    #         if j[0]%2 !=0 :return False
    #         for i in range(1,len(j)):
    #             if j[i] %2 !=0 :return False
    #             if j[i] >= j[i-1]:return False

    #     return True
    



    '''DFS postorder'''
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root.val %2 ==0:
            return False

        # True: odd level

        def dfs(root,flag):
            
            dfs(root.left,flag)
            dfs(root.right,flag)

            if flag:
                if root.val %2 ==0:
                    return False
            
            


        # dfs(root,True)
        return dfs(root,True)

# @lc code=end

