'''
Author: Zhou Hao
Date: 2021-02-18 22:51:47
LastEditors: Zhou Hao
LastEditTime: 2021-02-18 23:34:20
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''hashmap'''
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     hashmap = {}
    #     while head:
    #         #如果哈希表中第一次重复发现这个节点，这个节点就是重复节点，就是环的第一个节点
    #         if hashmap.get(head):return head

    #         hashmap[head] = 1
    #         head = head.next


    '''快慢指针法'''
    # 设链表环前有 aa 个节点，环内有 bb 个节点
    # 本题核心思路：走 a+nba+nb 步一定处于环的入口位置

    # 利用快慢指针 fastfast 和 slowslow，fastfast 一次走两步，slowslow 一次走一步
    # 当两个指针第一次相遇时，假设 slowslow 走了 ss 步，下面计算 fastfast 走过的步数
    # i. fastfast 比 slowslow 多走了 nn 个环：f = s + nbf=s+nb
    # ii. fastfast 比 slowslow 多走一倍的步数：f = 2sf=2s --> 跟上式联立可得 s = nbs=nb
    # iii. 综上计算得，f = 2nbf=2nb，s = nbs=nb
    # 也就是两个指针第一次相遇时，都走过了环的倍数，那么再走 aa 步就可以到达环的入口
    # 让 fastfast 从头再走，slowslow 留在原地，fastfast 和 slowslow 均一次走一步，当两个指针第二次相遇时，fastfast 走了 aa 步，slowslow 走了 a+nba+nb 步
    # 此时 slowslow 就在环的入口处，返回 slowslow


    def detectCycle(self, head: ListNode) -> ListNode:
        if (head == None) or  (head.next == None) :return None

        slow,fast = head,head
        while True:
            if not fast or not fast.next: 
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast :break      #第一次相遇


        fast = head 
        while fast != slow:         #第二次相遇
            fast = fast.next        #快指针每次走一步
            slow = slow.next
        
        return fast
        \home\zhouhao\Github_res\leetcode-zhou\142.环形链表-ii.py
# @lc code=end

