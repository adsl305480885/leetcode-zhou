'''
Author: Zhou Hao
Date: 2021-04-26 11:11:37
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 11:26:03
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0 :return ""


        def dfs(left:"剩下可用的左括号数量",right:"剩下可用的右扩号数量",track):
                
            if left > right:return      #剪枝
            if left <0 or right <0:return   #剪枝
            if left==0 and  right == 0:       #找到一个合法结果，终止条件
                res.append(track)
                return 

            track+='('
            dfs(left-1,right,track)
            track = track[:-1]
            
            track+=')'
            dfs(left,right-1,track)
            track = track[:-1]

        
        track = ""
        res = []
        dfs(n,n,track)
        return res
# @lc code=end

