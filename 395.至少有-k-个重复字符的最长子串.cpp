/*
 * @Author: Zhou Hao
 * @Date: 2021-05-06 13:51:25
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-06 14:48:45
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=395 lang=cpp
 *
 * [395] 至少有 K 个重复字符的最长子串
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

    //分治
    int longestSubstring(string s, int k) {
    // 遍历获取每个字符的个数，用于判断是否小于k
        unordered_map<char, int> m;
        for (auto& c : s)
        {
            m[c]++;
        }

        // 遍历把字符串按照小于k的数量拆分成多段，分开来解决
        vector<int> splits;
        int n = s.size();
        for (int i = 0; i < n; ++i)
        {
            if (m[s[i]] < k)
            {
                splits.push_back(i);       //把少于k个字符的索引存起来
            }
        }

        // 无需拆分，则返回整段字符串
        if (splits.size() <= 0)
        {
            return s.size();
        }


        // 返回最大长度
        int res = 0;
        int left = 0;
        
        //分治
        for (int i = 0; i < splits.size(); i++)
        {
            // 长度不包含这个split无效字符
            int len = splits[i] - left;
            // 至少要大于k，否则肯定是不满足的
            if (len >= k && len > res)
            {// 继续去找子串里最大值
                res = max(res, longestSubstring(s.substr(left, len), k));
            }
            left = splits[i] + 1;
        }
        
        // 考虑最后一段没考虑的情况
        if (left < n-1)
        {
            res = max(res, longestSubstring(s.substr(left, n-1-left+1), k));
        }

        return res;

    }
};
// @lc code=end

