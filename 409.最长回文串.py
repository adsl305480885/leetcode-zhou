'''
Author: Zhou Hao
Date: 2021-02-23 09:25:22
LastEditors: Zhou Hao
LastEditTime: 2021-02-23 11:29:52
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
class Solution:
    
    '''hashtable'''
    #1.用哈希表统计s中每个字母的次数
    # def longestPalindrome(self, s: str) -> int:  
    #     hashmap = {}
    #     for i in s:
    #         if i not in hashmap:
    #             hashmap[i] = 1
    #         else:
    #             hashmap[i] += 1
    #     print(hashmap)
    #     try:
    #         x = max([i for i in hashmap.values() if i %2 != 0])
    #     except:
    #         x = 0       #最大奇数次数

    #     sum ,flag= 0,True
    #     for k,v in hashmap.items():
    #         if v %2 == 0:
    #             sum +=v
    #         elif v %2 !=0 :
    #             if v ==x ==1 and flag:      #最大奇数是1，只加一次
    #                 sum += v
    #                 flag = False        #控制相加次数
    #             elif v == x  and x != 1 :       #最大奇数不是1，
    #                 if flag:        #最大的加一次
    #                     sum +=v
    #                     flag = False
    #                 else:           #其他最大的 加 x-1次
    #                     sum += v-1
    #             elif v<x and v>=3:  #比最大奇数小的奇数，如果>1，取其中的成对字符串
    #                 sum += (v-1)
    #     return sum


    def longestPalindrome(self, s: str) -> int:
        import collections
        hashmap = collections.Counter(s).values()
        # print(hashmap)

        res = sum([x if x%2==0 else x-1 for x in hashmap ])
        # print(res if res == len(s) else res +1)
        return res if res == len(s) else res +1
# @lc code=end

