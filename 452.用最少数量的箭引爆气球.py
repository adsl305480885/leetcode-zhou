'''
Author: Zhou Hao
Date: 2021-03-16 15:09:58
LastEditors: Zhou Hao
LastEditTime: 2021-03-16 16:40:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    '''排序+贪心,合并区间，减少区间'''
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     '''参考56.合并取区间'''
    #     length = len(points)
    #     if len(points) in [0,1]:
    #         return len(points)

    #     #升序
    #     sorted_points = sorted(points,key=lambda x:x[0]) 
    #     res = []
    #     res.append(sorted_points[0])


    #     #贪心遍历,找合并区间
    #     i = 1
    #     while i <length:
    #         if sorted_points[i][0] <= res[-1][1]:#重叠取交集
    #             res[-1][1] = min(res[-1][1],sorted_points[i][1])    #右区间取小
    #             i+=1
    #         else:
    #             res.append(sorted_points[i])
    #             i += 1

    #     #res是经过合并后的区间，各自独立
    #     return len(res)
        

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        '''增加箭的数量，不合并区间'''

        length = len(points)
        if length in [0,1]:
            return length

        #升序,按右坐标
        sorted_points = sorted(points,key=lambda x:x[1]) 

        res = 1
        right = sorted_points[0][1]        #第一个气球的右坐标  
        for i in sorted_points:
            if i[0] > right:        #如果不重叠，则保留右边气球的右坐标，箭+1
                right = i[1]
                res += 1
            #如果重叠，则一只箭就可以射爆这两个气球，右坐标还是左边左边气球的右坐标  
        # print(res)
        return res
# @lc code=end

