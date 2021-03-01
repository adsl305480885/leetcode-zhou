'''
Author: Zhou Hao
Date: 2021-02-27 13:55:27
LastEditors: Zhou Hao
LastEditTime: 2021-02-27 14:36:40
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=781 lang=python3
#
# [781] 森林中的兔子
#

# @lc code=start
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        import collections,math
        hashmap = collections.Counter(answers)
        # print(hashmap)

        res = 0
        for i,j in hashmap.items():
            res += math.ceil(j/(i+1))*(i+1)
        print(res)
        return res
# @lc code=end

