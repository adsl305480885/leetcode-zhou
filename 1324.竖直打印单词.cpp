/*
 * @Author: Zhou Hao
 * @Date: 2021-05-10 20:48:44
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-10 21:35:12
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1324 lang=cpp
 *
 * [1324] 竖直打印单词
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


    vector<string> printVertically(string s) {
        stringstream in(s);         //切割字符串
        vector<string> words;
        string _word;
        int maxlen = 0;
        while (in >> _word) {
            words.push_back(_word);     //切割后装进容器
            maxlen = max(maxlen, (int)_word.size()); //最长的字符串长度就是返回的长度
        }
        

        vector<string> ans;
        for (int i = 0; i < maxlen; ++i) {
            string concat;      //每一个元素
            
            for (string& word: words) {
                concat += (i < word.size() ? word[i] : ' ');
            }
            while (concat.back() == ' ') {      //弹出后面的空白
                concat.pop_back();
            }
            ans.push_back(move(concat));
        }
        return ans;
    

    }
};
// @lc code=end

