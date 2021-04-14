'''
Author: Zhou Hao
Date: 2021-04-14 15:43:29
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 17:16:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import List


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     # 计算链表长度
    #     # 1.find new head ( 倒数第k个节点)
    #     # 2.原链表中新节点右边的直接接到新节点右边
    #     # 3.原链表中新节点左边的先保留，然后接到后面
    #     if not head or k == 0 :return head
        
    #     cur = head
    #     length = 0
    #     while cur:
    #         length += 1
    #         cur = cur.next

    #     if k % length ==0 or length ==1: 
    #         return head     #等于链表长度就是翻了一圈和原来一样
    #     elif k > length:k%=length   #最后需要翻转的几步


    #     #找倒数第k个节点作为新的首节点
    #     cur = head
    #     count = 0
    #     left = None
    #     while cur:
    #         count += 1

    #         if length+1-count == k:
    #             new_head = ListNode(cur.val)    #找到新节点

    #         elif length + 1 -count < k:
    #             temp = new_head
    #             while temp.next:
    #                 temp = temp.next
    #             temp.next = ListNode(cur.val)

    #         elif length +1 -count > k:
    #             if not left:
    #                 left = ListNode(cur.val)
    #             else:
    #                 temp = left
    #                 while temp.next:
    #                     temp = temp.next
    #                 temp.next = ListNode(cur.val)
                    
    #         cur = cur.next
            

    #     cur = new_head
    #     while cur.next:
    #         cur = cur.next
    #     cur.next = left
    #     return new_head




    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # 计算链表长度
        # 1.find new head ( 倒数第k个节点)
        # 2.原链表中新节点右边的直接接到新节点右边
        # 3.原链表中新节点左边的先保留，然后接到后面
        if not head or k == 0 :return head
        
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next

        if k % length ==0 or length ==1: 
            return head     #等于链表长度就是翻了一圈和原来一样
        elif k > length:k%=length   #最后需要翻转的几步


        #找倒数第k个节点作为新的首节点
        cur = head
        count = 0
        while cur:
            count += 1

            if length+1-count == k:
                new_head = cur      #新首节点和右边的点
                
                temp = head     #新首节点左边的链表断尾
                num = 0
                while temp:
                    num += 1
                    if length+1-num == k+1:
                        temp.next = None
                        break
                    temp =temp.next
                    
                break

            cur = cur.next
        
        cur = new_head      #接上链表
        while cur.next:
            cur = cur.next
        cur.next = head


        return new_head


# @lc code=end

