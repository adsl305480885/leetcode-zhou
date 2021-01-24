'''
Author: Zhou Hao
Date: 2021-01-21 15:04:22
LastEditors: Zhou Hao
LastEditTime: 2021-01-21 17:21:26
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    '''
    杨辉三角形性质：
        1，每行首尾是1
        2.第几行就有几个数字
        3.每个数字等于上一行的左右两个数字之和，可用此性质写出整个杨辉三角。
            即第 n 行的第 i 个数等于第 n-1 行的第 i-1 个数和第 ii 个数之和
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        result = [] #总的列表

        for i in range(numRows):      #遍历每一行
            row_list = []   #空列表用来存储每一行的元素
            if i == 0:
                row_list.append(1)
                result.append(row_list)

            else:
                for r in range(i+1):  #计算这一行的每个数字
                    if r < i and r > 0:
                        #每一行的中间元素
                        row_list.insert(r, result[i-1][r]+result[i-1][r-1])
                    else:
                        #每一行的首尾元素都是1
                        row_list.insert(r,1)


                result.append(row_list)

        return result   
                    
            
        
# @lc code=end

