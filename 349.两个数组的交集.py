'''
Author: Zhou Hao
Date: 2021-02-05 14:35:28
LastEditors: Zhou Hao
LastEditTime: 2021-02-05 16:10:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    #方法一：hash-table
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     hashmap = {}
    #     for i in nums1:
    #         if i not in hashmap:
    #             hashmap[i] = 1
                
    #     for i in nums2:
    #         if i in hashmap:
    #             hashmap[i] = 2 

    #     print(hashmap)
    #     return [k for k,v in hashmap.items() if v !=1]


    #方法二：set
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     return set(nums1)&set(nums2)
        

    #方法三:双指针+排序，给每个数组分配一个指针
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     nums1,nums2 = sorted(nums1),sorted(nums2)   #排序，升序
    #     print(nums1,nums2)
    #     res = []
        
    #     index1 = index2 =0
    #     while index1 < len(nums1) and index2 <len(nums2):
    #         if nums1[index1] == nums2[index2]:
    #             if  not res or nums1[index1] != res[-1]:       #避免重复添加
    #                 res.append(nums1[index1])
    #             index1+=1
    #             index2 +=1
    #         elif nums1[index1] > nums2[index2]:
    #             index2+=1
    #         else:index1+=1
            
    #     print(res)
    #     return res
        


    #方法四:二分查找+排序，给每个数组分配一个指针
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2 = sorted(nums2)   #排序升序
        res = []
        
        def binarySerch(target) -> bool:
            left , right = 0,len(nums2)-1
            while left <= right:
                mid = (left+right) // 2
                if nums2[mid] == target:return True
                elif nums2[mid] < target:
                    left = mid+1
                elif nums2[mid] > target:
                    right = mid-1
            
            return False
        
        for i in nums1:
            # if binarySerch(i):
            print(binarySerch(i))
            if binarySerch(i):
                res.append(i)


        print('\n')
        return list(set(res))
    


# @lc code=end

