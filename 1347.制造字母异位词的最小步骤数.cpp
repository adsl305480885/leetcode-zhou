/*
 * @Author: Zhou Hao
 * @Date: 2021-05-06 15:54:39
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-06 16:36:19
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1347 lang=cpp
 *
 * [1347] 制造字母异位词的最小步骤数
 */

// @lc code=start
#include<vector>
#include<string>
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<numeric>
using namespace std;
class Solution {
public:
    int minSteps(string s, string t) {
        int length = s.size(),res=0;
        unordered_map<char,int> s_map;
        for(int i = 0;i<length;i++) s_map[s[i]]++;

        for(int i = 0;i<length;i++)
        {
            if(s_map[t[i]]) s_map[t[i]]--;
            else res++;
        }

        return res;

    }
};
// @lc code=end

