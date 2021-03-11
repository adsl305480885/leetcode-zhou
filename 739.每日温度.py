'''
Author: Zhou Hao
Date: 2021-03-11 12:14:03
LastEditors: Zhou Hao
LastEditTime: 2021-03-11 13:53:04
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
class Solution:
    '''
        本题应该用个「单调递减栈」来实现。
        建立「单调递减栈」，并对原数组遍历一次：
        如果栈为空，则把当前元素放入栈内；
        如果栈不为空，则需要判断当前元素和栈顶元素的大小：
        如果当前元素比栈顶元素大：说明当前元素是前面一些元素的「下一个更大元素」，则逐个弹出栈顶元素，直到当前元素比栈顶元素小为止。
        如果当前元素比栈顶元素小：说明当前元素的「下一个更大元素」与栈顶元素相同，则把当前元素入栈。
        栈里面需要保存元素在数组中的下标，而不是具体的数字。因为需要根据下标修改结果数组 
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []      #栈保存下标,栈下标所指的元素单减
        n = len(T)
        res = [0] * n

        for i,t in enumerate(T):
            # if not stack:stack.append(t)

            while stack and t > T[stack[-1]]:
                temp_index = stack.pop()
                res[temp_index] =  i - temp_index    #记录被抛出元素的下一个更大元素
            stack.append(i)

        # print(res)
        return res
        
# @lc code=end

