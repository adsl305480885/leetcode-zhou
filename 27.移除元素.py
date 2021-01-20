'''
Author: Zhou Hao
Date: 2021-01-19 21:31:34
LastEditors: Zhou Hao
LastEditTime: 2021-01-19 21:44:10
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    '''方法一:倒序遍历
        如果需要在正向遍历的过程中，删除list的多个元素，需要判断，如果删除，index值不能变，比较麻烦
        反向遍历就不会存在这个问题
    '''
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     for i in range(len(nums)-1,-1,-1):  #倒序遍历
    #         if nums[i] == val:nums.pop(i)

    #     return len(nums)
        

    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        

        
# @lc code=end

