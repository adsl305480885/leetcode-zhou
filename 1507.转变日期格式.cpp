/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 16:26:38
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 16:42:14
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1507 lang=cpp
 *
 * [1507] 转变日期格式
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
#include<unordered_set>
#include<unordered_map>
using namespace std;


class Solution {
public:
    string reformatDate(string date) {
        unordered_map<string, string> s2month = {
            {"Jan", "01"},
            {"Feb", "02"},
            {"Mar", "03"},
            {"Apr", "04"},
            {"May", "05"},
            {"Jun", "06"},
            {"Jul", "07"},
            {"Aug", "08"},
            {"Sep", "09"},
            {"Oct", "10"},
            {"Nov", "11"},
            {"Dec", "12"}
        };

        stringstream ss(date);      //用stringstream切割字符串
        string year, month, day;
        ss >> day >> month >> year;
        month = s2month[month];
        day.pop_back();
        day.pop_back();
        if (day.size() == 1) {
            day = "0" + day;
        }
        return year + "-" + month + "-" + day;

    }
};
// @lc code=end

