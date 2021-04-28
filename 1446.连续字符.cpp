/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 13:00:31
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 13:07:15
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1446 lang=cpp
 *
 * [1446] 连续字符
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;


class Solution {
public:

    //双指针滑动窗口
    int maxPower(string s) {
        int res = 0;
        int length = s.size();
        for(int i =0;i<length;)
        {
            int j =i;
            while(j<length && s[j]==s[i]) j++;
            if(j-i > res) res = j-i;
            i=j;
        }
        return res;
    }   
};
// @lc code=end

