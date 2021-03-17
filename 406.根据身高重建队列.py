'''
Author: Zhou Hao
Date: 2021-03-17 20:51:57
LastEditors: Zhou Hao
LastEditTime: 2021-03-17 21:37:41
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution:
    # 一个人的k值实际上与身高更矮的人的位置无关，
    # 所以如果身高比他更高的人已经排好队了，
    # 这个人加入当前队列的位置就可以根据k值确定了。
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_2 = sorted(people, key = lambda x: (-x[0], x[1]))
        # print(people_2)

        new_people = [people_2[0]]    # 这个人是从前往后、从上往下看到的第一个人
        
        for i in people_2[1:]:  
            new_people.insert(i[1], i)  #此时比i 高的人已经排好队了，根据k确定i的位置  

            # print(new_people)
        return new_people
# @lc code=end

