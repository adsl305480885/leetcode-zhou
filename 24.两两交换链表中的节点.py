'''
Author: Zhou Hao
Date: 2021-03-13 21:14:28
LastEditors: Zhou Hao
LastEditTime: 2021-04-01 17:15:01
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #     #递归
    # def swapPairs(self, head: ListNode) -> ListNode:

    #     #  如果链表中至少有两个节点，则在两两交换链表中的节点之后，
    #     # 原始链表的头节点变成新的链表的第二个节点，
    #     # 原始链表的第二个节点变成新的链表的头节点。

    #     # 用 head 表示原始链表的头节点，新的链表的第二个节点，
    #     # 用 newHead 表示新的链表的头节点，原始链表的第二个节点，
    #     # 则原始链表中的其余节点的头节点是 newHead.next。
    #     # 令 head.next = swapPairs(newHead.next)，表示将其余节点进行两两交换，
    #     # 交换后的新的头节点为 head 的下一个节点。然后令 newHead.next = head，
    #     # 即完成了所有节点的交换。最后返回新的链表的头节点 newHead。


    #     if not head or not head.next:   #链表中没有节点了或者只有一个节点了
    #         return head
    #     else:       #进行交换，注意先后顺序

    #         newHead = head.next   #节点二变成新链表的头节点
    #         '''这里必须先找到第三个节点，才能给newHead.next赋值'''
    #         head.next = self.swapPairs(newHead.next)      #第三个节点开始进行下一轮交换
    #         newHead.next = head   #节点一变成新链表的第二个节点       


    #         return newHead
            


    '''两两交换顺序类似栈先进后出,用栈来迭代'''
    def swapPairs(self, head):
        if not head or not  head.next:
            return head

        p = ListNode(-1)
        # 用stack保存每次迭代的两个节点
        # head指向新的p节点，函数结束时返回head.next即可
        cur,head,stack = head,p,[]
        while cur and cur.next:
            # 将两个节点放入stack中
            _,_ = stack.append(cur),stack.append(cur.next)
            # 当前节点往前走两步
            cur = cur.next.next
            # 从stack中弹出两个节点，然后用p节点指向新弹出的两个节点
            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next
            
            
        # 注意边界条件，当链表长度是奇数时，cur就不为空	
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next


        
# @lc code=end

