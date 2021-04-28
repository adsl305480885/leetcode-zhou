/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 12:32:02
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 12:58:35
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1455 lang=cpp
 *
 * [1455] 检查单词是否为句中其他单词的前缀
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        vector<string> vec;
        string temp;

        for(int i =0;i<sentence.size();i++)     //按空格用vector切分字符串
        {
            if(sentence[i]!=' ') temp += sentence[i];
            else
            {
                vec.push_back(temp);
                temp = "";
            }
        }
        vec.push_back(temp);

        for(int i =0;i<vec.size();i++)
        {
            if(vec[i].substr(0,searchWord.size()) == searchWord) return i+1;
        }
        return -1;
    }
};
// @lc code=end

