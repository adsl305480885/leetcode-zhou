#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    #笨方法
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    #     if not head :
    #         return

    #     queue = []      #队列
    #     while head:
    #         queue.append(head)
    #         head = head.next    

    #     queue.pop(-n)       #队列去掉要删除的节点
        
    #     new = ListNode(0)
    #     node = new
    #     #把队列重新构造出链表
    #     for i in  range(len(queue)):
    #         node.next = queue[i]
    #         node = node.next
    #     node.next = None        #封尾
    #     return new.next



    #递归
    def removeNthFromEnd(self, head, n):
        global  i   #加了global后，整个递归里面，i的值是通用的
        i = 0
        if not head :
            return None
        
        head.next = self.removeNthFromEnd(head.next,n)
        #递归到最后一个节点，从尾节点往头节点走
        i+=1        #记数，倒数
        print('iiiiii',i)

        if i==n:
            print('++++',head)
            return head.next
        else:
            print('****',head)
            return  head



        
# @lc code=end

