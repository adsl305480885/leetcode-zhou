/*
 * @Author: Zhou Hao
 * @Date: 2021-05-06 14:49:32
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-06 15:06:34
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 *//*
 * @lc app=leetcode.cn id=424 lang=cpp
 *
 * [424] 替换后的最长重复字符
 */

// @lc code=start
#include<vector>
#include<string>
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
using namespace std;
class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26,0);

        // maxCount记录字符出现次数最多那个字符的次数，res储存最大的窗口大小
        int left = 0,res = 0,maxCount = 0;  
        for(int i=0; i<s.size();i++)
        {
            count[s[i] - 'A'] ++;
            // 比较之前记录的最大数 和 当前字符的数量
            maxCount = max(maxCount,count[s[i]- 'A']);
            // 若当前窗口大小 减去 窗口中最多相同字符的个数 大于 k 时
            while(i-left+1 - maxCount > k)
            {
                count[s[left]-'A'] --;
                left++; // 滑动窗口
            }
            res = max(res,i-left+1);
        }
        return res;
    }
};
// @lc code=end

