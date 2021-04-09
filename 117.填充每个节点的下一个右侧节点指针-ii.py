'''
Author: Zhou Hao
Date: 2021-04-09 09:19:00
LastEditors: Zhou Hao
LastEditTime: 2021-04-09 13:34:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
    '''BFS '''
    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:return root

    #     cur_lay = [root]        #the initial lay is root lay
    #     while cur_lay:      # 
    #         next_lay = []
            
    #         if len(cur_lay) > 1:    #pass the root lay
    #             for i in range(len(cur_lay[:-1])):      
    #                 cur_lay[i].next = cur_lay[i+1]  #update the node.next in the cur_lay

    #         for node in cur_lay:    #get the next_lay
    #             if node.left:
    #                 next_lay.append(node.left)
    #             if node.right:
    #                 next_lay.append(node.right)
                    
    #         cur_lay = next_lay      #update the cur lay

    #     return root



    '''DFS'''
    def connect(self, root: 'Node') -> 'Node':
        last = []
        def DFS(node, depth):
            if not node: return

            # 例如 last[0] last[1]都有 depth = 3
            if len(last) < depth:
                last.append(node)
            else:
                node.next = last[depth -1]
                last[depth - 1] = node
            

            DFS(node.right, depth + 1)
            DFS(node.left, depth + 1)
            
            return
        
        DFS(root, 1)
        return root


# @lc code=end

