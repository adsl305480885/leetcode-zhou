/*
 * @Author: Zhou Hao
 * @Date: 2021-05-10 20:27:53
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-10 20:48:13
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=647 lang=cpp
 *
 * [647] 回文子串
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
    int palindrome(const string& s,int left,int right)
        {
            int num = 0;
            while (left>=0 && right<s.size() && s[left]==s[right])
            {
                left --;
                right ++;
                num++;
            }
            return num;// 返回以 s[l] 和 s[r] 为中心的回文字串数量
        }

    int countSubstrings(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); i++) 
        {
            int res_1 = palindrome(s,i,i);  //奇数中心
            int res_2 = palindrome(s,i,i+1);    //偶数中心
            res += (res_1+res_2);
        }
        return res;
    }
};
// @lc code=end

