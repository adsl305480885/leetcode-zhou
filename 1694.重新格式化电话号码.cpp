/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 14:53:58
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 15:06:59
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1694 lang=cpp
 *
 * [1694] 重新格式化电话号码
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
public:
    /*
        找规律
        最后剩下一个/三个/两个的时候都不用管
        只需要考虑最后剩下四个，最后判断下倒数第二个位置是否是-，若是，将倒数第二个位置和倒数第三个位置互换
    
    */
    string reformatNumber(string number) {
        string str, res;
        for (auto &s : number) {
            if (s != ' ' && s != '-') str += s;
        }
        
        res += str[0];
        for (int i = 1; i < str.size(); ++i) {
            if (i % 3 == 0) res += '-';
            res += str[i];
        }
        
        if (res[res.size() - 2] == '-') swap(res[res.size() - 2], res[res.size() - 3]); 
        return res;
    }
};
// @lc code=end

