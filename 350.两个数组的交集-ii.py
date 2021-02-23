'''
Author: Zhou Hao
Date: 2021-02-23 21:41:00
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 22:56:39
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    '''hashtable'''
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     hashmap_1 = {}
    #     for n in nums1:
    #         if n not in hashmap_1:    
    #             hashmap_1[n] = 1
    #         else:
    #             hashmap_1[n] += 1

    #     res = []
    #     for n in nums2: 
    #         if n in hashmap_1 and hashmap_1[n] >0:
    #             hashmap_1[n] -=1
    #             res.append(n)
    #     return res
        

    #字典相交 & 
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import collections
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        res = num1 & num2

        # print(list(res.keys()))
        return res.elements()       #字典得所有元素 

# @lc code=end

