#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #双指针，一前一后
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    #     if not head:
    #         return      #空链表就直接返回
        
    #     pre = head      #前后两个指针，指向前后两个节点
    #     last = pre.next     #当pre是尾节点得时候，last指向None
        
    #     while last:     #后面节点不为空的时候就循环,如果last是None，pre就是尾节点
    #         if pre.val == last.val:
    #             pre.next = last.next        #通过改变指针的指向来删除节点
    #             last = last.next
    #         else:        #两个指针依次往后挪一位
    #             pre = pre.next
    #             last = last.next
    #     return head



    #单指针
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return

        cur = head  
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
            
# @lc code=end

