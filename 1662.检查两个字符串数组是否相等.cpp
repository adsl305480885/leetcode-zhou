/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 14:42:55
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 14:50:22
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1662 lang=cpp
 *
 * [1662] 检查两个字符串数组是否相等
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {


public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string word_1, word_2;
        for(int i =0;i<word1.size();i++)word_1+=word1[i];
        for(int i =0;i<word2.size();i++) word_2+=word2[i];

        return word_1 == word_2;     
    }
};
// @lc code=end

