#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
# 自定义节点类
class Node(object):
    def __init__(self, item):
        self.val = item
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__length = 0  # 保存链表长度
        self.__head = Node(None)  # 哑节点(节点头部,但不是首节点),指向空表示空链表,

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        #  0 <=  index <= self.__length-1
        if index < 0 or index >= self.__length:
            return -1
        cur = self.__head
        for i in range(index+1):
            cur = cur.next  # 循环，找到这个索引对应的节点
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        return self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        return self.addAtIndex(self.__length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            index = 0
        elif index > self.__length:
            return

        node = Node(val)  # 生成要插入的节点

        # 通过循环找到要插入的位置
        pre = self.__head  # 首节点
        for i in range(index):  # 这里不用index+1,如果index是0,那pre就是头部的哑节点
            pre = pre.next  # 指向下一个节点

        # 退出循环的时候，pre是要插入地方的上一个节点
        node.next = pre.next
        pre.next = node  # 注意先后顺序
        self.__length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index >=self.__length:     #0<=索引<self.__length
            return
        pre = self.__head
        for i in range(index):      #退出循环的时候,pre指向要删除节点的前一个节点
            pre = pre.next
        pre.next = pre.next.next        #删除第index个节点，改变指针指向
        self.__length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
