'''
Author: Zhou Hao
Date: 2021-03-17 17:43:46
LastEditors: Zhou Hao
LastEditTime: 2021-03-17 20:23:24
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#

# @lc code=start
class Solution:
#     1.首先遍历S，用字典记录每个字符出现的次数，转换为列表从多到少排序。# dic = [["A",5],["B",3],["C",1]]
# 2.如果出现最多的字符个数大于(len(S)+1)//2，直接返回空字符串。
# 3.从S里选择字符添加到新字符串s末尾，贪心的想法：每次先加一个dic里次数最多的字符，然后加一个其他字符隔开，一直到次数最多的字符全部添加完毕。
# 4.每次添加都在dic里减去当前字符的次数，如果当前状态次数最多的字符添加完，减完后dic里记录的次数不是从大到小排序，则用冒泡的方法把dic[0] 往后移，一直到排序成立。
# 5.循环添加，直到s和S的长度相等，返回s
    def reorganizeString(self, S: str) -> str:
        
        fuck = len(S) + 1
        from collections import Counter
        times = Counter(S)
        a = times.most_common() #返回列表，列表里面的元素是元组[(key,value)],按次数降序
        a = [list(i) for i in a]
        if a[0][1] > fuck//2:return ''


        res = ' '
        long = 1
        while long!= fuck:
            i = 0
            while i < len(a) :
                if a[i][0] != res[-1]:
                    res += a[i][0]
                    long += 1
                    a[i][1] -= 1
                    if  a[i][1] == 0:   #某个字母没有了，就pop掉，然后重新排序降序
                        a.pop(i)
                        a = sorted(a,reverse=True,key = lambda x:x[1])
                    break
                else:
                    i +=1

        return res[1:]
# @lc code=end

