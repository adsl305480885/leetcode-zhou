'''
Author: Zhou Hao
Date: 2021-02-16 12:57:21
LastEditors: Zhou Hao
LastEditTime: 2021-02-16 13:20:06
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #快慢指针，快指针走二步，慢指针走一步
    #快指针到达尾部的时候，慢指针必然在中间
    # def middleNode(self, head: ListNode) -> ListNode:
        # fast_point = head
        # slow_point = head

        # while (fast_point != None and fast_point.next != None):
            # slow_point = slow_point.next
            # fast_point = fast_/point.next.next
        # print(slow_point)
        # return slow_point
    
    
    #单指针，先遍历一遍得到链表长度
    def middleNode(self, head: ListNode) -> ListNode:
        n,cur_1,cur_2 = 0,head,head
        while cur_1:
            n += 1
            cur_1 = cur_1.next
            
        k = 0
        while k< n//2:
            k += 1
            cur_2 = cur_2.next
        return cur_2
# @lc code=end

