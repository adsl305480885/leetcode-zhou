'''
Author: Zhou Hao
Date: 2021-04-14 19:03:17
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 19:24:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    '''两个辅助链表'''
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:return head
        p =less= ListNode(0)    #小链表的第一个节点
        q =more= ListNode(0)    #大链表的第一个节点

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                more.next = head
                more = more.next

            head = head.next

        more.next = None
        less.next = q.next        #因为big的首节点是0
        return p.next



    '''双指针原地修改'''
    #TODO

# @lc code=end

