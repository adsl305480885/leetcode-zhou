'''
Author: your name
Date: 2020-12-19 23:31:11
LastEditTime: 2020-12-19 23:40:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \leetcode-zhou\496.下一个更大元素-i.py
单调栈和hash
'''
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, hashmap = list(), dict()
        for i in nums2:
            while len(stack) != 0 and stack[-1] < i:hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i,-1) for i in nums1]

        
# @lc code=end

