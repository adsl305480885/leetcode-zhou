'''
Author: Zhou Hao
Date: 2021-04-19 21:28:19
LastEditors: Zhou Hao
LastEditTime: 2021-04-19 21:57:35
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1418 lang=python3
#
# [1418] 点菜展示表
#

# @lc code=start
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        new_orders = sorted(orders,key=lambda x:int(x[1]))

        hashmap = {}  # {桌号:{菜名:数量 }}
        footItem = []

        for order in new_orders:
            if order[2] not in footItem:
                footItem.append(order[2])

            if order[1] not in hashmap:
                hashmap[order[1]] = {}

            hashmap[order[1]][order[2]] = \
                        hashmap[order[1]].get(order[2], 0) + 1


        footItem = sorted(footItem)
        res = [['Table']+footItem]
        for k ,v in hashmap.items():
            temp = [k]
            for food in footItem:
                temp.append(str(v.get(food,0)))
            res.append(temp)

        # print(res)
        return res

        
# @lc code=end

