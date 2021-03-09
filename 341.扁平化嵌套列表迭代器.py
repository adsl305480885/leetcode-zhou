'''
Author: Zhou Hao
Date: 2021-03-09 21:26:39
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 21:50:48
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    '''结合173,二叉搜索树迭代器'''

    
    #方法一:正向DFS
    # def __init__(self, nestedList: [NestedInteger]):
        
    #     def dfs(root):
    #         #直接深度优先遍历,也类似N叉树遍历
    #         for n in root:
    #             if n.isInteger():
    #                 self.midList.append(n.getInteger())
    #             else:
    #                 dfs(n.getList())

    #     self.midList = []
    #     dfs(nestedList)
    #     self.index = -1
    
    # def next(self) -> int:
    #     self.index += 1
    #     return self.midList[self.index]
    
    # def hasNext(self) -> bool:
    #     return self.index < len(self.midList)-1


    #方法二:逆向DFS
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(root):
            for n in root[::-1]:
                if n.isInteger():
                    self.midList.append(n)
                else:
                    dfs(n.getList())

        self.midList = []
        dfs(nestedList)
        
        
    def next(self) -> int:
        return self.midList.pop()
    
    def hasNext(self) -> bool:
        return self.midList != []

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

