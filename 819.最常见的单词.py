'''
Author: Zhou Hao
Date: 2021-01-16 22:57:09
LastEditors: Zhou Hao
LastEditTime: 2021-01-17 17:16:31
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    '''方法一：'''
    # def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    #     import string

    #     test = [x if x not in string.punctuation else ' ' 
    #             for x in paragraph ]    #把标点转为空格，后面统一去掉空格
    #     new = ''.join(test) #list to str

    #     str_list =  new.lower().split() #不区分大小写，去掉空格

    #     hashmap = {}
    #     for i in set(str_list):
    #         hashmap[i] = str_list.count(i)
    
    #     for ban in banned:  #如果有ban键就删除
    #         if ban in hashmap:
    #             del hashmap[ban]

    #     return max(hashmap,key=hashmap.get)
        
    '''方法二:哈希'''
    


    '''方法三，正则，思路和方法一一样'''
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower() # 标点符号替换为空格
        print(paragraph)
        paragraph = paragraph.split()
        dicts = {}
        for char in paragraph: # 统计paragraph里单词出现的次数，这段代码也可以直接使用collections.Counter函数代替
            if char not in dicts: # dicts = collections.Counter(paragraph)
                dicts[char] = 1
            else:
                dicts[char] += 1
        for i in dicts: # j将在banned里的键所对应的值，置为-1，这样在比较大小时，可以将其忽略。
            if i in banned:
                dicts[i] = -1
        return max(dicts, key = dicts.get) # 获得字典dicts中value的最大值所对应的键

        

        
# @lc code=end
