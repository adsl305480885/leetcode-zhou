'''
Author: Zhou Hao
Date: 2021-03-08 21:53:03
LastEditors: Zhou Hao
LastEditTime: 2021-03-08 23:42:41
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    # 把此问题中的空节点理解成叶子节点,出度+，入度-
    # 根结点的入度为0出度为2，其他非叶子结点的入度为1出度为2，
    # 叶子节点入度为1出度为0。因为根节点多出来一个出度，
    # 所以初始化度为1，一个非叶子节点时度+1，
    # 加入一个空节点（叶子节点）时度-1，
    # 如果度为0，即达到出度入度相等，已经形成一颗二叉树
    # def isValidSerialization(self, preorder: str) -> bool:
    #     degree = 1

    #     for node in preorder.split(','):
    #         # print(i)
    #         if degree == 0:
    #             return False

    #         if node == "#":
    #             degree -= 1
    #         else:
    #             degree += 1

    #     return degree == 0
        

    # 二叉树中，叶子节点（0出度节点）  = 2度（出度）节点+1
    def isValidSerialization(self, preorder: str) -> bool:

        leaf , nonleaf = 0,0
        for i in preorder.split(','):
            if leaf > nonleaf:  #前序遍历过程中，叶子节点数量小于2度节点
                return False
            if i == '#':        #把'#'看成叶子节点
                leaf += 1
            else:       # 数字看成2度节点
                nonleaf += 1
        return leaf == (nonleaf +1)



    # 方法三:栈
    # 方法四:树的顶点数等于树的边数+1。
# @lc code=end

