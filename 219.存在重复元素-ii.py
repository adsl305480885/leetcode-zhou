#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    '''哈希表:
        字典的键 = 列表的值
        字典的值= 列表的索引
    '''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                if i - hashmap[nums[i]] <= k:
                    return True
                else:
                    hashmap[nums[i]] = i
            else:
                hashmap[nums[i]] = i

        return False


# @lc code=end

