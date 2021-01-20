'''
Author: Zhou Hao
Date: 2021-01-20 22:31:41
LastEditors: Zhou Hao
LastEditTime: 2021-01-20 22:57:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # list(set(b) - set(a))   
        # 使用  "-"  运算求a与b的差(补)集： 求b中有而a中没有的元素，输出：[6]
        
        few =  set([x for x in range(1,len(nums)+1)])- set(nums)
        print(few)

        return list(few)
# @lc code=end

