'''
Author: Zhou Hao
Date: 2021-04-06 11:59:16
LastEditors: Zhou Hao
LastEditTime: 2021-04-06 14:59:15
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    '''recursion,preorder,DFS'''
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:return None
    #     self._help(root.left,root.right)
    #     return root


    # def _help(self,node1,node2):
    #     if not node1 or not node2:return None

    #     node1.next = node2  #recursion,preorder

    #     self._help(node1.left,node1.right)
    #     self._help(node2.left,node2.right)
    #     self._help(node1.right,node2.left)



    '''BFS,iteration'''
    def connect(self, root: 'Node') -> 'Node':
        if not root:return root

        cur_lay = [root]        #the initial lay is root lay
        while cur_lay:      # 
            next_lay = []
            
            if len(cur_lay) > 1:    #pass the root lay
                for i in range(len(cur_lay[:-1])):      
                    cur_lay[i].next = cur_lay[i+1]  #update the node.next in the cur_lay

            for node in cur_lay:    #get the next_lay
                if node.left:
                    next_lay.append(node.left)
                if node.right:
                    next_lay.append(node.right)
                    
            cur_lay = next_lay      #update the cur lay

        return root


# @lc code=end

