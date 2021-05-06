/*
 * @Author: Zhou Hao
 * @Date: 2021-05-06 13:20:13
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-06 13:48:38
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=438 lang=cpp
 *
 * [438] 找到字符串中所有字母异位词
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
    vector<int> findAnagrams(string s, string p) 
    {
        vector<int> res;
        int left =0,right = 0;
        unordered_map<char,int> needs;
        unordered_map<char,int> windows;
        for(auto c: p ) needs[c]++;
        int match = 0;

        
        while(right<s.size())       //直到rigth到达尽头就退出循环
        {
            char c1 = s[right];
            if(needs.count(c1))
            {
                windows[c1]++;
                if(windows[c1] == needs[c1]) match++;
            }
            right++;            //不满足条件的时候滑右


            while(match == needs.size())        //满足条件的时候滑左
            {
                if(right - left == p.size()) res.push_back(left);   //更新结果
            
                char c2 = s[left];
                if(needs.count(c2))
                {
                    windows[c2]--;
                    if(windows[c2]<needs[c2]) match--;
                }
                left++;
            }

        }

        return res;

    }
};
// @lc code=end

