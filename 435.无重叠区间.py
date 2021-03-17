'''
Author: Zhou Hao
Date: 2021-03-17 09:06:23
LastEditors: Zhou Hao
LastEditTime: 2021-03-17 09:47:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    '''贪心，区间问题。参考 6.划分区间     452.用最少量的箭引爆气球, 763划分字母空间'''
    # def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    #     #按做坐标升序排列
    #     sort_inter = sorted(intervals,key=lambda x:x[0])
    #     res = 0
    #     m = len(sort_inter)

    #     i = 1

    #     while i < m and m >1:
    #         if sort_inter[i][0] < sort_inter[i-1][1]:   #重叠
    #             #删除尾部较大的区间（贪心）
    #             if sort_inter[i][1] > sort_inter[i-1][1]:
    #                 sort_inter.pop(i)
    #             else:
    #                 sort_inter.pop(i-1)
                
    #             #这里不用i-1,因为删除一个元素后，下一个元素的索引就是当前i
    #             res += 1
    #             m -= 1
    #         else:
    #             i+=1
        
    #     return res
        




    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        #按右坐标升序排列
        sort_inter = sorted(intervals,key=lambda x:x[1])
        
        rest = 0        #需要保留的区间数量
        right = -float('inf')       #无穷小的浮点型
        for i in sort_inter:
            if i[0] >= right: #不重叠,保留区间+1,右坐标更新为新的右坐标
                right = i[1]
                rest += 1

        return len(intervals) - rest

        
        
# @lc code=end

