'''
Author: Zhou Hao
Date: 2021-03-16 20:21:01
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 20:49:26
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    '''贪心'''
    # 1、两个数组之差的总和必须大于等于0，否则不能完成绕行 
    # 2、一个站的收益如果小于0，肯定不能作为起点；而连续的多个站也可以等效地看做一个站，如果其累积收益小于0，就跳过，寻找下一个。
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #先判断能不能绕行
        if sum(gas) < sum(cost):return -1 

        #如果能绕行，计算每个加油站剩下的油量
        remains = [gas[i] - cost[i] for i in range(len(gas))]
        start = 0
        cur = 0

        for i in range(len(remains)):   #贪心遍历每个加油站，判断每个加油站是否可以作为起点
            cur += remains[i]
            if cur < 0 :        #寻找非0剩余油量加油站作为起点
                start = i + 1
                cur = 0

        # print(start)
        return start
# @lc code=end

