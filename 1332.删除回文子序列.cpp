/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 12:08:13
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 12:28:25
 * @Description: file contenti
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1332 lang=cpp
 *
 * [1332] 删除回文子序列
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
using namespace std;


class Solution {
public:
    // int removePalindromeSub(string s) {
    //     string b(s);
    //     reverse(b.begin(),b.end());
    //     if(s == "") return 0;
    //     else if(s == b) return 1;
    //     else return 2;
    // }
    

    int removePalindromeSub(string s) {
        if(s=="") return 0;

        int length = s.size();
        for(int i =0; i<length/2;i++)
        {
            if(s[i]!=s[length-i-1]) return 2;
        }
        return 1;
    }
};
// @lc code=end

