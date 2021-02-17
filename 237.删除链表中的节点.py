'''
Author: Zhou Hao
Date: 2021-02-16 12:45:16
LastEditors: Zhou Hao
LastEditTime: 2021-02-16 12:58:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #当前节点的值=下个节点，当前节点的指针指向下下个节点
        node.val = node.next.val
        node.next = node.next.next
        
# @lc code=end

