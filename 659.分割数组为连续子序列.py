'''
Author: Zhou Hao
Date: 2021-03-16 16:48:46
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 17:03:35
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=659 lang=python3
#
# [659] 分割数组为连续子序列
#

# @lc code=start
class Solution:
    '''贪心'''
    def isPossible(self, nums: List[int]) -> bool:
        #遍历每个数字，如果能接着上一个子序列，就插入到上个子序列后面
        #如果不能，就插入到前面，这样下个数字优先插入到短的子序列。
        stack = []
        for i in nums:  
            if not stack:stack.append([i])
            else:
                for s in stack:
                    if s[-1] + 1 ==i:
                        s.append(i) #插入到上个子序列后面
                        break
                else:
                    stack.insert(0,[i])     #优先插入到前面，插入到短的子序列


        for s in stack:
            if len(s)<3:
                return False

        return True
# @lc code=end

