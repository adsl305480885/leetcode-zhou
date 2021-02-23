'''
Author: Zhou Hao
Date: 2021-02-18 23:37:59
LastEditors: Zhou Hao
LastEditTime: 2021-02-18 23:55:49
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #双指针，指向奇偶
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return head
        double_head = head.next
        
        single,double = head,double_head
        while  double and double.next:
            
            #更新节点，注意顺序，先奇数后偶数
            single.next = double.next
            single = single.next

            double.next = single.next
            double = double.next
            
        single.next = double_head
        return head
# @lc code=end

