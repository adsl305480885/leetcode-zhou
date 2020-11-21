#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head
        while(curr):
            anchor = curr.val
            flag = False
            while(curr.next):
                if curr.next.val == anchor:
                    flag = True
                    curr = curr.next
                else:
                    break
            if flag: # if duplicates, relink
                prev.next = curr.next
            else: # if single, move prev
                prev = curr
            curr = curr.next
        return dummy.next


# @lc code=end

