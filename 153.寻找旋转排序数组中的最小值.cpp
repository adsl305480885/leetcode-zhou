/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 16:02:39
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-07 16:13:55
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=153 lang=cpp
 *
 * [153] 寻找旋转排序数组中的最小值
 */

// @lc code=start
#include<vector>
#include<string>
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<queue>
#include<numeric>
using namespace std;

class Solution {
public:

    //暴力
    // int findMin(vector<int>& nums) {
    //     int min_ = nums[0];
        
    //     for(auto i :nums){
    //         min_ = min(min_,i);
    //     }
    //     return min_;
    // }
    

    //二分,按索引二分
    int findMin(vector<int>& nums) {
        int left = 0 , right = nums.size()-1;

        while(left<right)
        {
            int mid = left + (right-left)/2;
            if(nums[mid] < nums[right]) right = mid;
            else left = mid+1;
        }
        return nums[left];
    }

};
// @lc code=end

