'''
Author: Zhou Hao
Date: 2021-03-09 17:03:43
LastEditors: Zhou Hao
LastEditTime: 2021-03-09 18:48:56
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    '''方法一:二叉搜索树中,左节点<根<右节点. 所以直接中序遍历就行'''
    # def __init__(self, root: TreeNode):
    #     #得到中序遍历后的升序列表
    #     def dfs(root):
    #         if not root:return

    #         dfs(root.left)
    #         self.midList.append(root.val)
    #         dfs(root.right)

    #     self.midList = []
    #     dfs(root)
    #     self.index = -1
        

    # def next(self) -> int:
    #     self.index += 1
    #     return self.midList[self.index]

    # def hasNext(self) -> bool:
    #     return self.index < len(self.midList) -1 



    '''方法二:
    二叉搜索树中,左节点<根<右节点,反中序遍历(右根左)得到一个降序列表
    '''
    def __init__(self, root: TreeNode):
        #得到反中序遍历后的降序列表
        def dfs(root):
            if not root:return

            dfs(root.right)
            self.midList.append(root.val)
            dfs(root.left)

        self.midList = []
        dfs(root)

        

    def next(self) -> int:
        return self.midList.pop()

    def hasNext(self) -> bool:
        return self.midList != []



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

