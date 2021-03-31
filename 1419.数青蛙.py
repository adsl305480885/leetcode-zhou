'''
Author: Zhou Hao
Date: 2021-03-31 21:13:26
LastEditors: Zhou Hao
LastEditTime: 2021-03-31 21:59:46
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1419 lang=python3
#
# [1419] 数青蛙
#

# @lc code=start
class Solution:

    # c,r,o,a,k分别表示遍历到当前位置时这几个字母出现的次数。
    # 每次遍历过程中当且仅当c>=r>=o>=a>=k时才符合要求。
    # now表示当前存在的青蛙个数，即遇到c时加一，叫完以后(遇到k)减一。
    # 遍历完后now应为0表示每次叫声都有头有尾，记录now的最大值即为答案。
    # def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
    #     c = r=o=a=k =0
    #     now = res = 0

    #     for i in croakOfFrogs:
    #         if i == 'c':
    #             c+=1
    #             now += 1
    #             res = max(res,now)
    #         elif i == 'r':
    #             r+=1
    #         elif i == 'o':
    #             o+=1
    #         elif i == 'a':
    #             a+= 1
    #         elif i == 'k':
    #             k+=1
    #             now -=1

    #         if not c>=r>=o>=a>=k:   #依序
    #             return -1
    #     return res if now==0 else -1
        



    '''greedy'''
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # 贪心思想体现在，出现一个字符，则将它放入最早等待使用该字符的单词中。
        # 本题的难点在于如何高效记录当前出现的未完成的单词，并用于查找。
        # 解决这个问题的思路，和最长递增子序列有一些类似。
        # 1.设置变量c，r，o，a
        # 2.当出现变量对应的字符，则将该变量+1，前面的字符（如果有的话）-1
        # 3.最多的青蛙数，就是这些变量和的最大值
        # 4.如果出现负数，则返回-1

        if len(croakOfFrogs) %5 != 0:return -1
        c = r=o=a=0

        res = 0

        for i in croakOfFrogs:
            if i == 'c':
                c+=1
            elif i == 'r':
                c-=1
                r+=1
            elif i == 'o':
                r -= 1
                o += 1
            elif i == 'a':
                o -= 1
                a+=1
            else:
                a-=1
            
            if c<0 or r <0 or o <0 or a <0 :
                return -1
            res = max(res,c+r+o+a)
            
        return res

# @lc code=end

