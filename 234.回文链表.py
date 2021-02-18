'''
Author: Zhou Hao
Date: 2021-02-18 11:53:43
LastEditors: Zhou Hao
LastEditTime: 2021-02-18 22:21:55
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #把值复制到列表中，然后判断列表是不是回文列表
    # def isPalindrome(self, head: ListNode) -> bool:
    #     values = []
    #     cur = head
    #     while cur:#遍历链表
    #         values.append(cur.val)
    #         cur = cur.next

    #     return values == values[::-1]   #判断是不是回文

        
        
        

    #递归
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head

        def helper(right=head):
            if not right:
                return True
            res = helper(right.next)
            if self.left.val != right.val:
                return False
            self.left = self.left.next
            return res
        return helper()

# @lc code=end

