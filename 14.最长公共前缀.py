'''
Author: Zhou Hao
Date: 2021-01-06 20:09:14
LastEditors: Zhou Hao
LastEditTime: 2021-01-06 21:23:27
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    
    '''方法一'''
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     if not strs:return ""
    #     res = ""
    #     ss = list(map(set,zip(*strs)))
    #     # 1. *strs直接获得列表中每个字符串
    #     # 2. zip从前到后依次取每个字符串的一位组成元组，元组的个数等于strs中最短的字符串长度
    #     #    把每个字符串的相同位置取出来凑成一个元组
    #     # 3. map(set,)对所有元组去重，对每个位置所有元素进行去重
    #     #    如果去重后长度=1就是公共字符串，否则不是
    #     #    如果第一位的元组长度！=1，那就没有公共字符串
    #     for i in ss:
    #         i = list(i)
    #         if len(i)>1:break
            
    #         res += i[0]
    #     return res


    '''方法二'''
    #比较字符串的asci码，从第一位字母开始比较
    # def longestCommonPrefix(self, strs):
    #     if not strs: return ""
    #     s1 = min(strs)
    #     s2 = max(strs)
    #     for i,x in enumerate(s1):
    #         if x != s2[i]:
    #             return s2[:i]
    #     return s1





# @lc code=end

