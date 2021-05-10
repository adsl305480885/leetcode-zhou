/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 11:51:38
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-10 20:28:31
 * @Description: file content/
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=5 lang=cpp
 *
 * [5] 最长回文子串
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

    string palindrome(const string& s,int left,int right)
    {
        while (left>=0 && right<s.size() && s[left]==s[right])
        {
            left --;
            right ++;
        }
         // 返回以 s[l] 和 s[r] 为中心的最⻓回文串
        return s.substr(left+1, right-left-1);

    }

    //中心扩散法
    string longestPalindrome(string s) {
        string res;
        for (int i = 0; i < s.size(); i++) {
            // 以 s[i] 为中心的最⻓回文子串
            string s1 = palindrome(s, i, i);
            // 以 s[i] 和 s[i+1] 为中心的最⻓回文子串
            string s2 = palindrome(s, i, i + 1);
            // res = longest(res, s1, s2)
            res = res.size() > s1.size() ? res : s1;
            res = res.size() > s2.size() ? res : s2;
        }
        return res;

    }
};
// @lc code=end

