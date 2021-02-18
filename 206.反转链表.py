'''
Author: Zhou Hao
Date: 2021-02-18 08:54:57
LastEditors: Zhou Hao
LastEditTime: 2021-02-18 11:50:59
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #
    # def reverseList(self, head: ListNode) -> ListNode:
    #     cur,pre = head,None
    #     while cur:
    #         print(pre,cur.next,cur)
    #         pre,cur.next,cur = cur,pre,cur.next
    #         print(pre,cur.next,cur)
    #     return pre


    '''迭代法'''
    # 遍历链表，指针 cur 指向当前节点，指针 pre 指向cur的前驱节点
    # 初始化 pre 和 cur
    # temp 存储后继结点
    # 更新 pre 和 cur
    # 反转操作，更新后的 pre 的后驱节点为 temp
    def reverseList(self, head: ListNode) -> ListNode:
        pre,cur = None,head
        while cur:
            temp = cur.next 
            cur.next = pre
            pre = cur
            cur = temp
            # cur.next = pre
        return pre

# @lc code=end

