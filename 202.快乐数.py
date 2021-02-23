'''
Author: Zhou Hao
Date: 2021-02-22 22:40:41
LastEditors: Zhou Hao
LastEditTime: 2021-02-22 23:53:47
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    
    '''哈希'''
    # 给一个数字 nn，它的下一个数字是什么？
    # 按照一系列的数字来判断我们是否进入了一个循环。
    # 第 1 部分我们按照题目的要求做数位分离，求平方和。
    # 第 2 部分可以使用哈希集合完成。每次生成链中的下一个数字时，我们都会检查它是否已经在哈希集合中。

    # 如果它不在哈希集合中，我们应该添加它。
    # 如果它在哈希集合中，这意味着我们处于一个循环中，因此应该返回 false。
    def isHappy(self, n: int) -> bool:
        
        hashmap = {}

        def get_next_n(n):
            sum = 0
            while n > 0 :
                n,i = divmod(n,10)
                sum += i*i
            # print(sum)         
            return sum        
        
        n = get_next_n(n)
        while True:
            if n != 1 :
                if n not in hashmap:
                    hashmap[n] = 1
                    n = get_next_n(n)
                else:
                    return False
            elif n ==1:return True


    '''快慢指针'''
# @lc code=end

