'''
Author: Zhou Hao
Date: 2021-02-26 14:58:40
LastEditors: Zhou Hao
LastEditTime: 2021-02-26 23:44:14
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    '''滑动窗口+哈希'''
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) == 0:return 0
    #     set_s = set(s)
    #     if len(set_s) == len(s):return len(s)

    #     left,right = 0,1
    #     res = 0
    #     hashmap = {}
    #     while left<len(s) and right < len(s):
            
    #         if s[left]  not in hashmap:
    #             hashmap[s[left]] = 1

    #         if s[right]  not in hashmap:
    #             if right < len(s)-1:
    #                 # print('bbb',s[left:right+1])
    #                 hashmap[s[right]] = 1
    #                 right += 1
    #             elif right ==len(s)-1:                
    #                 res = max(res,right-left+1)
    #                 return res
    #         elif s[right] in hashmap:
    #             # print('ccc',s[left:right+1])
    #             res = max(res,right-left)
    #             left +=1
    #             right = left +1
    #             hashmap.clear()
            

    #     return res
        
        


    #    遍历字符串，用哈希表记录每个字符的索引
    # left用于记录字符串的最左侧索引，maxLen用于记录子串的最大长度
    # 如果当前遍历到的字符已在哈希表中存在，说明是个重复字符
    # 子串的左侧索引应该从该字符前一次出现的索引的下一个位置开始
    # 但是因为前一个字符可能已不在子串中，还要和left自身取一下最大值
    # 即，left = max(left, hashmap[c] + 1)
    # 子串的长度即为当前索引 i - 左侧索引 left + 1, maxLen取子串长度的最大值
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap = {}
        left = maxLen = 0
        for i, c in enumerate(s):
            if c in hashmap:
                left = max(left, hashmap[c] + 1)
                # left = hashmap[c] +1
            hashmap[c] = i
            maxLen = max(maxLen, i - left + 1)
        return maxLen
# @lc code=end

