'''
Author: Zhou Hao
Date: 2021-03-03 09:40:31
LastEditors: Zhou Hao
LastEditTime: 2021-03-03 17:21:59
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''递归'''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:return l2 #终止条件
        if not l2:return l1

        #减小规模
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
# @lc code=end

