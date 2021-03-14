'''
Author: Zhou Hao
Date: 2021-02-18 08:54:57
LastEditors: Zhou Hao
LastEditTime: 2021-03-14 22:10:22
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
        pre,cur = None,head     #在遍历过程中，pre一直是cur的前面的节点
        while cur:
            temp = cur.next 
            cur.next = pre
            pre = cur           #每次迭代把pre往后推一位
            cur = temp          #把cur往后推一位
            # cur.next = pre
        return pre
        

    '''递归'''
    #使用递归函数，一直递归到链表的最后一个结点，该结点就是反转后的头结点，记作 retret .
    # 此后，每次函数在返回的过程中，让当前结点的下一个结点的 nextnext 指针指向当前节点。
    # 同时让当前结点的next指针指向NULL ，从而实现从链表尾部开始的局部反转
    # 当递归函数全部出栈后，链表反转完成
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if not head.next:
    #         return head
    #     else :
    #         res = self.reverseList(head.next)       #先递归
    #         head.next.next = head       #再改当前节点
    #         head.next = None      #断开以前的连接
    #         return res  #翻转之后的头节点,也就是翻转前的尾节点

# @lc code=end

