'''
Author: Zhou Hao
Date: 2021-01-23 11:37:50
LastEditors: Zhou Hao
LastEditTime: 2021-01-23 23:00:16
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

# @lc code=start
class Solution:
    '''方法一：笨方法
        排序后正负分开
    '''
    # def maximumProduct(self, nums: List[int]) -> int:
    #     if len(nums) == 3:
    #         return nums[0]*nums[1]*nums[2]
        
    #     nums_zheng = sorted([x for x in nums if x >=0])
    #     nums_fu = sorted([x for x in nums if x < 0])
    #     # nums_0 = [x for x in nums if x==0]

    #     res = 1
    #     if len(nums_fu) == 0:
    #         res = nums_zheng[-1]*nums_zheng[-2]*nums_zheng[-3]
    #     elif len(nums_zheng) == 0 :
    #         res = nums_fu[-1]*nums_fu[-2]*nums_fu[-3]
    #     else:
    #         if len(nums_fu) == 1:   #只有一个负数，三正
    #             res = nums_zheng[-1]*nums_zheng[-2]*nums_zheng[-3]
    #         elif len(nums_zheng) == 1:   #只有一个正数，两负一正
    #             res = nums_zheng[-1]*nums_fu[1]*nums_fu[0] 
    #             # res_2 = nums_zheng[-1]*nums_zheng[-2]*nums_zheng[-3]

    #             # if res_1>res_2:res = res_1
    #             # else:res = res_2
    #         else:   #多正多负
    #             if len(nums_zheng) <=2: #两正一负
    #                 res = nums_zheng[-1]*nums_fu[1]*nums_fu[0]
    #             else:
    #                 res_1 = nums_zheng[-1]*nums_fu[1]*nums_fu[0] 
    #                 res_2 = nums_zheng[-1]*nums_zheng[-2]*nums_zheng[-3]

    #                 if res_1>res_2:res = res_1
    #                 else:res = res_2

    #     return res
    
    '''
        方法二:
        将nums排序
        如果全为正数或全为负数，最大三个数的乘积为a
        如果存在两个以上负数，两个最小负数与最大正数的乘积b
        三数乘积的最大值肯定为：max(a,b)
    '''
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a = nums[-1]*nums[-2]*nums[-3]
        b = nums[0]*nums[1]*nums[-1]
        return max(a,b)

# @lc code=end

