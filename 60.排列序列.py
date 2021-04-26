'''
Author: Zhou Hao
Date: 2021-04-26 11:28:36
LastEditors: Zhou Hao
LastEditTime: 2021-04-26 16:31:02
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 排列序列
#

# @lc code=start
class Solution:
    

        
    '''回溯,笨方法，参考全排列'''
    # def getPermutation(self, n: int, k: int) -> str:
    #     res = 1
    #     for i in range(1,n):        #计算每个数字当首位时有多少个结果
    #         res *=i     

    #     sum = 0
    #     begin = 0
    #     for i in range(1,n+1):
    #         sum+=res
    #         if sum >=k:
    #             begin = i
    #             # print('首位数字应该是:\t',i)
    #             break
    #     k = k - (sum-res)

    #     nums = [i for i in range(1,n+1) if i != begin]
    #     if not nums:return str(begin)
    #     n-=1

    #     self.times = 0

    #     def dfs(nums,track):
    #         if len(track) == n:
    #             self.times += 1
    #             return

    #         for i in range(n):
    #             if nums[i] in track:
    #                 continue

    #             track.append(nums[i])
    #             dfs(nums,track)
    #             if self.times == k:
    #                 return track
    #             track.pop()

    #     track = []
    #     a = dfs(nums,track)
    #     return str(begin)+''.join([str(i) for i in a])



    '''递归推导每一位的数字，每个数字就相当于树的每一层'''
    def getPermutation(self, n: int, k: int) -> str:
        global rets,total   #
        rets = ""
        total = sum(range(n+1))

        def dfs(n,k,nums):
            global rets,total
            if n == 1:
                rets += str(total)
                return rets

            res = 1
            for i in range(1,n):        #计算每个数字当首位时有多少个结果
                res *=i     
            # print('计算每个数字当首位时有多少个结果:\t',res)
            
            sum = 0
            for i in range(len(nums)):
                sum+=res
                if sum >=k:
                    begin = nums[i]
                    rets += str(nums[i])
                    total -= nums[i]
                    break
            k = k - (sum-res)           #确定当前数字后还剩的k
            # print('首位数字应该是:\t',nums[i])
            # print('确定当前数字后还剩的k:\t',k,'\n')
            n-=1
            
            nums = [j for j in nums if j != begin]
            dfs(n,k,nums)

        dfs(n,k,range(1,n+1) )   
        return rets
        
# @lc code=end

