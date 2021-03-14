'''
Author: Zhou Hao
Date: 2021-03-14 20:54:38
LastEditors: Zhou Hao
LastEditTime: 2021-03-14 22:54:13
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    '''重点复习！！！！！！！！'''
    # https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/bu-bu-chai-jie-ru-he-di-gui-di-fan-zhuan-lian-biao/

    #递归
    def  reverseN(self,head,n):#翻转头n个节点
            if n == 1:      #n==1就是已经走完了前n个节点，这是结束条件
                self.temp = head.next  #记录下一个节点,记录第 n + 1 个节点
                return head
            
            # 以 head.next 为起点，需要反转前 n - 1 个节点
            last =self.reverseN(head.next,n-1)  #递归一次就-1，递归结束后返回反转后的头节点
            head.next.next = head
            head.next  = self.temp   #连接后驱节点 

            return last

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        if left == 1:   
            #此时找到了第m个节点
            #对于第m个节点，就是翻转链表开头的n个节点
            return self.reverseN(head,right)


        head.next  = self.reverseBetween(head.next,left-1,right-1)
        return head

# @lc code=end

