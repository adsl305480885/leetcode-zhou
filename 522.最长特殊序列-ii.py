'''
Author: Zhou Hao
Date: 2021-01-12 13:49:15
LastEditors: Zhou Hao
LastEditTime: 2021-01-12 14:44:18
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=522 lang=python3
#
# [522] 最长特殊序列 II
#

# @lc code=start
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
#       1.把所有重复的字符（用list2记录重复字符串，后面需要使用）串删除。
#       2.把第一步删除后的列表中所有属于list2的子字符串删除。（这一步较难）
#       3.剩下都是属于特殊序列，只需要找出最长的即可。
        list2 = []
        list3 = []
        for i in strs:
            if strs.count(i) >= 2:
                list2.append(i)
        for i in list2:
            strs.remove(i)
        #上述操作删除重复字符串
        

        for i in strs:
            for j in list2:
                temp_len = len(i)
                for k in range(temp_len):
                    if i[k] not in j:
                        break
                    if i[k] in j and k != temp_len -1:
                        j = j[j.index(i[k])+1:]
                if k == temp_len - 1 and i[k] in j:
                    list3.append(i)
                    break
        print(strs,"\n",list3)
        for j in list3:
            strs.remove(j)
        #上述操作删除子字符串


        #print(strs)
        #下述操作找最长字符串（即最长特殊序列）
        if len(strs) == 0:
            return -1
        len_max = strs[0]
        for i in range(1,len(strs)):
            if len(len_max) < len(strs[i]):
                len_max = strs[i]
        return len(len_max)
        
# @lc code=end

