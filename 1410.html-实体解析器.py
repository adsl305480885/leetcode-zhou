'''
Author: Zhou Hao
Date: 2021-03-10 21:58:04
LastEditors: Zhou Hao
LastEditTime: 2021-03-10 22:03:29
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=1410 lang=python3
#
# [1410] HTML 实体解析器
#

# @lc code=start
class Solution:
    #直接正则
    def entityParser(self, text: str) -> str:
        import re
        text = re.sub('\&apos;',"'",text)
        text = re.sub('\&quot;','"',text)
        text = re.sub('\&gt;','>',text)
        text = re.sub('\&lt;','<',text)
        text = re.sub('\&frasl;','/',text)
        text = re.sub('\&amp;','&',text)
        return text
# @lc code=end

