'''
Author: Zhou Hao
Date: 2021-03-12 09:45:30
LastEditors: Zhou Hao
LastEditTime: 2021-03-12 10:03:53
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1019 lang=python3
#
# [1019] 链表中的下一个更大节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        '''单调递减栈，
        参考  503，739
        建立「单调递减栈」，并对原数组遍历一次,栈存放下标
        如果栈为空，则把当前元素放入栈内；
        如果栈不为空，则需要判断当前元素和栈顶元素的大小：
        如果当前元素比栈顶元素大：说明当前元素是前面一些元素的「下一个更大元素」，则逐个弹出栈顶元素，直到当前元素比栈顶元素小为止。
        如果当前元素比栈顶元素小：说明当前元素的「下一个更大元素」与栈顶元素相同，则把当前元素入栈。
        栈里面需要保存元素在数组中的下标，而不是具体的数字。因为需要根据下标修改结果数组 
        '''

        #栈元素列表化
        val_list= []
        while head:
            val_list.append(head.val)
            head = head.next
            
        #单调递减栈，存索引
        stack = []
        res = [0] * len(val_list)
        for i,v in enumerate(val_list):
            while stack and val_list[ stack[-1]] < v:
                res[stack.pop()] = v

            stack.append(i)
            
        return res
        
        

# @lc code=end

