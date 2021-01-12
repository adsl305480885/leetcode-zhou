'''
Author: Zhou Hao
Date: 2021-01-12 13:13:10
LastEditors: Zhou Hao
LastEditTime: 2021-01-12 13:27:33
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=657 lang=python3
#
# [657] 机器人能否返回原点
#

# @lc code=start
class Solution:
    '''方法一：掉包'''
    # def judgeCircle(self, moves: str) -> bool:
    #     if moves.count('U') == moves.count('D') and \
    #     moves.count('L') == moves.count('R'):
    #         return True
    #     else:return False
        



    '''方法二，哈希字典计数'''
    def judgeCircle(self, moves: str) -> bool:
        hashmap = {
        'U':0,
        'D':0,
        'L':0,
        'R':0,
    }

        for i,v in enumerate(moves):
            if not hashmap.get(v):
                hashmap[v] = 1
            else: 
                hashmap[v] +=1
        print(hashmap)
                
        if hashmap['U'] == hashmap['D'] and hashmap['L'] == hashmap['R']:
            return True
        else: return False


        
# @lc code=end

