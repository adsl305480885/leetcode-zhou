'''
Author: Zhou Hao
Date: 2021-02-18 22:27:11
LastEditors: Zhou Hao
LastEditTime: 2021-02-18 22:50:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''hashtab'''
    # def hasCycle(self, head: ListNode) -> bool:
    #     hashmap = {}
    #     while head:
    #         if hashmap.get(head):return True
            
    #         hashmap[head] = 1#这里是把节点当作键，因为可能存在相同的值
    #         head = head.next

    #     return False


    '''提示链表节点数目小于10000'''
    # def hasCycle(self, head: ListNode) -> bool:
        # sum = 0
        # while head:
        #     sum +=1
        #     if sum >10000:return True
        #     head = head.next
        # return False


    '''快慢指针，双指针'''
    def hasCycle(self, head: ListNode) -> bool:
        if (head == None) or  (head.next == None) :return False 


        #快指针每次都走，慢指针两次走一次
        fast,slow,flag = head,head,False
        while fast:
            fast = fast.next
            
            if flag:
                slow = slow.next
                flag = False
            else:flag = True

            if fast == slow:
                return True
        return False
# @lc code=end

