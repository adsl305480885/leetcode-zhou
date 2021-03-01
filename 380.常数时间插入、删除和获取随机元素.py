'''
Author: Zhou Hao
Date: 2021-03-01 18:57:42
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 20:47:09
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    #集合
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not  in self.a:
            self.a.add(val)
            return True
        else:return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.a:
            self.a.remove(val)
            return True
        else:return False 
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import choice
        return choice(list(self.a))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

