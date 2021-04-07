'''
Author: Zhou Hao
Date: 2021-04-07 21:38:37
LastEditors: Zhou Hao
LastEditTime: 2021-04-07 22:54:53
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    '''
        because of BST's speciality , we don't need "null" in the serialize 
        and we can select the left and right in deserialize,
    '''


    '''DFS  predoer'''
    # def serialize(self, root: TreeNode) -> str:
    #     """Encodes a tree to a single string.
    #     """
    #     if not root:
    #         return 'None'
    #     return str(root.val) + ',' + str(self.serialize(root.left)) + ',' + str(self.serialize(root.right))
        
        
    # def deserialize(self, data: str) -> TreeNode:
    #     """Decodes your encoded data to tree.
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




    '''DFS  predoer'''
    # def serialize(self, root: TreeNode) -> str:
    #     res = []
    #     def dfs(root):
    #         if not root:
    #             return []
    #         res.append(root.val)

    #         dfs(root.left)
    #         dfs(root.right)

    #     dfs(root)
    #     print(res)
        
    #     return ','.join([str(i) for i in res])


        
    # def deserialize(self, data: str) -> TreeNode:
    #     if not data :return[]
        
    #     def dfs(data):
    #         if not data:
    #             return None
            
    #         root = TreeNode(data[0])
    #         left = [i for i in data if i <data[0]]
    #         right = [i for i in data if i> data[0]]
    #         root.left = dfs(left)
    #         root.right = dfs(right)
        
    #         return root
    #     datalist = data.split(',')
    #     datalist = [int(i) for i in datalist]
    #     return dfs(datalist)


    '''DFS postorder'''
    # def serialize(self, root: TreeNode) -> str:
    #     res = []

    #     def dfs(root):
    #         if not root:
    #             return []

    #         dfs(root.left)
    #         dfs(root.right)
    #         res.append(root.val)

    #     dfs(root)
    #     print(res)
        
    #     return ','.join([str(i) for i in res])


        
    # def deserialize(self, data: str) -> TreeNode:
    #     if not data :return[]
        
    #     def dfs(data):
    #         if not data:
    #             return None
            
    #         root = TreeNode(data[-1])
    #         left = [i for i in data if i <data[-1]]
    #         right = [i for i in data if i> data[-1]]
    #         root.left = dfs(left)
    #         root.right = dfs(right)
        
    #         return root
    #     datalist = data.split(',')
    #     datalist = [int(i) for i in datalist]
    #     return dfs(datalist)
        



    '''BFS'''
    #TODO
    # def serialize(self, root):
    #     if not root:return []
        

    #     cur,res = [root],[]
    #     while cur:
    #         node = cur.pop(0)
    #         if node:
    #             res.append(node.val)
    #             cur.append(node.left)
    #             cur.append(node.right)
    #         else:
    #             res.append('#')

    #     return ','.join([str(i) for i in res])



    # def deserialize(self, data):
    #     if not data:return []

    #     datalist = data.split(',')
    #     print(datalist)
    #     for d in datalist:
    #         print(d)

    #     root = TreeNode(data[0])
    #     cur = [root]
    #     i = 1

    #     while cur:
    #         node = cur.pop(0)

    #         # print(data[i])
    #         if data[i] != '#':
    #             node.left = TreeNode(datalist[i])
    #             cur.append(node.left)
    #         i+=1

    #         if data[i] != '#':
    #             node.right = TreeNode(datalist[i])
    #             cur.append(node.right)
    #         i+=1
    #     return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

