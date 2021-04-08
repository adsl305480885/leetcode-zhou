'''
Author: Zhou Hao
Date: 2021-04-07 13:40:22
LastEditors: Zhou Hao
LastEditTime: 2021-04-08 09:22:57
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:


    '''DFS,preorder'''
    # def serialize(self, root):
    #     """Encodes a tree to a single string.
        
    #     :type root: TreeNode
    #     :rtype: str
    #     """

    #     if not root:
    #         return 'None'
    #     return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        
        

    # def deserialize(self, data):

    #     '''looks like 654.'''
    #     """Decodes your encoded data to tree.
        
    #     :type data: str
    #     :rtype: TreeNode
    #     """


    #     def dfs(dataList):
    #         val = dataList.pop(0)
    #         if val == 'None':
    #             return None
    #         root = TreeNode(int(val))
    #         root.left = dfs(dataList)
    #         root.right = dfs(dataList)
    #         return root

    #     dataList = data.split(',')
    #     return dfs(dataList)




    '''DFS,preorder'''
    # def serialize(self, root):
    #     res = []
    #     def dfs(root):
    #         if not root: 
    #             res.append('#')
    #             return None

    #         res.append(root.val)

    #         dfs(root.left)
    #         dfs(root.right)

    #     dfs(root)
    #     return res



    # def deserialize(self, data):

    #     def dfs(data):
    #         if not data:return None

    #         first = data.pop(0)
    #         if first == '#':return None
    #         root = TreeNode(first)

    #         root.left = dfs(data)
    #         root.right  = dfs(data)

    #         return root

    #     return dfs(data)
        



    '''DFS postorder'''
    # def serialize(self, root):
    #     res = []
        
    #     def dfs(root):
    #         if not root:
    #             res.append('#')
    #             return None

    #         dfs(root.left)
    #         dfs(root.right)
    #         res.append(root.val)

    #     dfs(root)
    #     return res


    # def deserialize(self, data):
        
    #     def dfs(data):
    #         '''right -> left'''
    #         # because [left,right,root]

    #         if not data:return None
            
    #         last = data.pop()
    #         if last == '#':
    #             return None         
                
    #         root = TreeNode(last)
    #         root.right = dfs(data)          #first right,   data = [left,right]
    #         root.left = dfs(data)           # than left,    data = [left]

    #         return root

    #     return dfs(data)



    '''BFS'''
    def serialize(self, root):
        if not root:return []

        cur,res = [root],[]
        while cur:
            node = cur.pop(0)
            if node:
                res.append(node.val)
                cur.append(node.left)
                cur.append(node.right)
            else:
                res.append('#')

        return res



    def deserialize(self, data):
        if not data:return []
        

        print(data)

        root = TreeNode(data[0])
        cur = [root]
        i = 1

        while cur:
            node = cur.pop(0)

            if data[i] != '#':
                node.left = TreeNode(data[i])
                cur.append(node.left)
            i+=1

            if data[i] != '#':
                node.right = TreeNode(data[i])
                cur.append(node.right)
            i+=1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

