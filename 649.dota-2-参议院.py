'''
Author: Zhou Hao
Date: 2021-03-17 22:37:49
LastEditors: Zhou Hao
LastEditTime: 2021-03-18 10:59:44
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
class Solution:
    '''贪心，模仿刀人的过程'''
    # def predictPartyVictory(self, senate: str) -> str:
    #     senate =  [ str(s) for s in senate]
    #     cur = senate[0]     #记录当前的当权者
    #     temp = 0   #记录当权者的index


    #     while len(set(senate)) != 1:
    #         i = 0
    #         while i <len(senate):
    #             if senate[i] != cur:    #删除当权者后面的第一个其他阵营的
    #                 senate.pop(i)

    #                 if temp <i:
    #                     temp += 1          #当权者就变成下一个
                    
    #                 if len(senate) == 1:
    #                     return "Radiant" if senate[0] =='R' else "Dire"

    #                 if temp < len(senate): #更换当权者
    #                     cur = senate[temp]      
    #                 else:
    #                     temp = 0
    #                     cur = senate[temp]
    #             else:
    #                 i+=1 

                
    #     return "Radiant" if senate[0] =='R' else "Dire"
        


    '''贪心双队列'''
    def predictPartyVictory(self, senate: str) -> str:
        import collections
        queueR=collections.deque()
        queueD=collections.deque()
        n=len(senate)
        for i,c in enumerate(senate):
            if c=="R":
                queueR.append(i)
            else:
                queueD.append(i)
        
        while queueR and queueD:
            if queueR[0]<queueD[0]:
                queueD.popleft()
                queueR.append(queueR.popleft()+n)
            else:
                queueR.popleft()
                queueD.append(queueD.popleft()+n)
        
        return "Radiant" if queueR else "Dire"
# @lc code=end

