'''
Author: Zhou Hao
Date: 2021-03-01 16:08:03
LastEditors: Zhou Hao
LastEditTime: 2021-03-01 17:29:00
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    
    #笨比方法
    def getHint(self, secret: str, guess: str) -> str:
        length = len(secret)
        if secret == guess:
            return str(length)+'A'+'0B'

        bulls,cows = 0,0
        save_index = []
        for i in range(length):     #找公牛
            if secret[i] == guess[i]: 
                bulls+=1
            else:
                save_index.append(i)

        sa,ga = [],[]
        for i in range(length):     #去除公牛
            if i in save_index:
                sa.append(secret[i])
                ga.append(guess[i])

        for i in range(len(sa)):        #找母牛
            if ga[i] in sa: 
                cows += 1
                sa.remove(ga[i])
        return str(bulls)+'A'+str(cows)+'B'
        
    
# @lc code=end

