'''
Author: Zhou Hao
Date: 2021-03-08 11:35:41
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 15:54:00
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    '''本题应该用个「单调递减栈」来实现。
    建立「单调递减栈」，并对原数组遍历一次：
    如果栈为空，则把当前元素放入栈内；
    如果栈不为空，则需要判断当前元素和栈顶元素的大小：
    如果当前元素比栈顶元素大：说明当前元素是前面一些元素的「下一个更大元素」，则逐个弹出栈顶元素，直到当前元素比栈顶元素小为止。
    如果当前元素比栈顶元素小：说明当前元素的「下一个更大元素」与栈顶元素相同，则把当前元素入栈。
    栈里面需要保存元素在数组中的下标，而不是具体的数字。因为需要根据下标修改结果数组 
    '''


    #O(2n)
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
        #单调递减栈,栈保存下标,栈下标所指的元素单减
        # stack  = []
        # length = len(nums)
        # res = [-1] * length *2
        # nums = nums+nums

        # for i,v in enumerate(nums):#循环数组,遍历两次
        #     # print(i,v)
        #     while stack != []  and  v  >nums[stack[-1]]:        #当前数字>栈顶的数字
        #         res[stack.pop()] = v        #小数字的索引出栈,当前数字就是小数字的下一个更大元素
        #     stack.append(i)     #当前大数字入栈
        # return res[:length]
        

    #优化版,O(n)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack  = []
        length = len(nums)
        res = [-1] * length 
        nums = nums+nums    

        for i,v in enumerate(nums):#循环数组,遍历两次
            while stack != []  and  v  >nums[stack[-1]]:        #当前数字>栈顶的数字
                temp = stack.pop()
                if temp < length:res[temp] = v
                else:continue
                
            stack.append(i)     #当前大数字入栈
        return res

# @lc code=end

