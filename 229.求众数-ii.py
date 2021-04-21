'''
Author: Zhou Hao
Date: 2021-04-20 22:15:00
LastEditors: Zhou Hao
LastEditTime: 2021-04-20 22:26:11
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    # def majorityElement(self, nums: List[int]) -> List[int]:
    #     freq = len(nums)//3

    #     from collections import Counter

    #     count = Counter(nums)

    #     res = []
    #     for k,v in count.items():
    #         if v > freq:res.append(k)

    #     return res
        

    '''摩尔投票法'''
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1, cand2 = nums[0], nums[0]
        cnt1, cnt2 = 0, 0
        for num in nums:
            if cand1 == num:
                cnt1 += 1
            elif cand2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                cand1 = num
                cnt1 += 1
            elif cnt2 == 0:
                cand2 = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        majority_cnt = len(nums) // 3
        cnt1, cnt2 = 0, 0
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
                
        res = []
        if cnt1 > majority_cnt:
            res.append(cand1)
        if cnt2 > majority_cnt:
            res.append(cand2)
        return res


# @lc code=end

