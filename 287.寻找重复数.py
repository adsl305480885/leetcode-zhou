'''
Author: Zhou Hao
Date: 2021-04-13 20:22:04
LastEditors: Zhou Hao
LastEditTime: 2021-04-13 22:35:29
Description: file content
E-mail: 2294776770@qq.com
'''
#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
from typing import List


class Solution:
    '''hash'''
    # def findDuplicate(self, nums: List[int]) -> int:
    #     hashmap = {}
    #     for n in nums:
    #         hashmap[n] = hashmap.get(n,0)+1
    #         if hashmap[n] != 1:return n

    
    '''sort'''
    # def findDuplicate(self, nums: List[int]) -> int:
    #     if len(nums) == 2:return nums[0]
    #     nums = sorted(nums)
    #     print(nums)
        
    #     for i in range(len(nums[:-1])):
    #         print(nums[i])
    #         if nums[i] == nums[i+1]:
    #             return nums[i]


    '''二分'''
    # def findDuplicate(self, nums: List[int]) -> int:
    #     left,right =1, len(nums) -1   #根据值来二分
        
    #     while left <right:
    #         mid = (left + right)//2
    #         if nums.count(mid)>1:return mid
            
    #         small_nums = 0      #统计比mid小的数字
    #         for n in nums:
    #             if n<=mid:small_nums+=1

    #         if small_nums <= mid:   #如果小于mid的数字数量<=mid,说明重复数字在右边
    #             left = mid+1
    #         else:right = mid

    #     return left


    '''快慢指针找环的出口'''
    def findDuplicate(self, nums: List[int]) -> int:

        # 找环
        # 定义快慢指针slow=0,fast=0slow=0,fast=0
        # 进入循环：
        # slowslow每次走一步，即slow=nums[slow]slow=nums[slow]
        # fastfast每次走两步，即fast=nums[nums[fast]]fast=nums[nums[fast]]
        # 当slow==fastslow==fast时，退出循环。
        # 当快慢指针相遇时，一定在环内。此时假设slowslow走了kk步，则fastfast走了2k2k步。设环的周长为cc，则k\%c==0k%c==0。
        
        # 找环的入口：
        # 定义新的指针find=0find=0
        # 进入循环：
        # findfind每次走一步，即find=nums[find]find=nums[find]
        # slowslow每次走一步，即slow=nums[slow]slow=nums[slow]
        # 当两指针相遇时，即find==slowfind==slow，返回findfind
        # 为何相遇时，找到的就是入口：
        # 假设起点到环的入口(重复元素)，需要mm步。此时slowslow走了n+mn+m步，其中nn是环的周长cc的整数倍，所以相当于slowslow走了mm步到达入口，再走了nn步。所以相遇时一定是环的入口。


        slow=0
        fast=0
        while(1):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if(slow==fast):     #快慢指针相遇时，一定在环内
                break
        find=0          #慢指针置0
        while(1):
            find=nums[find]
            slow=nums[slow]
            if(find==slow):     #快慢指针再次相遇，必定是环的入口
                return find

        
        
# @lc code=end

