# @before-stub-for-debug-begin
from python3problem203 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 迭代/遍历
    # def removeElements(self, head: ListNode, val: int) -> ListNode:

    # if not head:
    #     return

    # begin = ListNode(0)     #哑节点,指向首节点
    # begin.next = head
    # pre = begin             #前后两个节点,哑节点
    # last = pre.next         #首节点

    # #这样写能包含所有情况/删除首节点/尾节点
    # while last:     #退出循环的时候last是None
    #     if last.val == val:
    #         pre.next = last.next        #执行删除操作
    #         last = pre.next
    #     else:
    #         pre = last
    #         last = last.next        #如果last是尾节点,则last.next为空，退出循环
    #     # print(begin.next)
    # # print(begin.next)     #指向头节点，就输出了整个链表
    # return begin.next



    # 递归,要有终止条件
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return

        head.next = self.removeElements(head.next, val)
        print(head.val) #6，递归到尾节点

        if head.val == val:
            #如果是要删除的节点，直接返回下一个节点
            #删除尾巴节点：返回None

            print('+++:',head.next)
            return head.next 
        else:
            print('****:',head)
            return head     #如果不是要删除的节点直接返回原节点
# @lc code=end
