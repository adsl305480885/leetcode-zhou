/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 16:15:28
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 16:25:12
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1374 lang=cpp
 *
 * [1374] 生成每种字符都是奇数个的字符串
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
#include<unordered_set>
using namespace std;
class Solution {
public:
    string generateTheString(int n) {
        string res;
        if(n%2 != 0)        //奇数
        { 
            for(int i =0;i<n;i++) res+='a';
            return res;
        }
        else        //偶数
            for(int i =0;i<n-1;i++) res+='a';
            res+='b';
            return res;

    }
};
// @lc code=end

