'''
Author: Zhou Hao
Date: 2021-04-14 12:30:17
LastEditors: Zhou Hao
LastEditTime: 2021-04-14 15:43:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    '''滑动窗口'''
    # def inWindow(self,window,target)->bool:
    #     from collections import Counter
    #     window_count = Counter(window)
    #     target_count = Counter(target)
    #     if target_count - window_count:
    #         return False
    #     else:
    #         return True


    # def minWindow(self, s: str, t: str) -> str:
    #     if not s:return ""
    #     if len(s)<len(t):return ""
    #     if s ==t :return s

    #     right = 0
    #     window  = ""
    #     hashset = [float('inf'),""]
        
    #     while right < len(s):
    #         window += s[right]
    #         right += 1

    #         while self.inWindow(window,t):
    #             length = len(window)
    #             if length<hashset[0]:
    #                 hashset[0] = length
    #                 hashset[1] = window
    #             window = window[1:]

    #     return hashset[1] 
        


    '''labuladong 滑动窗口模板'''
    #TODO:重点复习
    def minWindow(self, s: str, t: str) -> str:
        need=collections.defaultdict(int)
        for c in t:
            need[c]+=1
            
        needCnt=len(t)
        i=0
        res=(0,float('inf'))
        for j,c in enumerate(s):
            if need[c]>0:
                needCnt-=1
            need[c]-=1
            if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
                while True:      #步骤二：增加i，排除多余元素
                    c=s[i] 
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i<res[1]-res[0]:   #记录结果
                    res=(i,j)
                need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
                needCnt+=1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
        

# @lc code=end