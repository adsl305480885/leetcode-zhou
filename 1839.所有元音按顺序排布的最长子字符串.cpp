/*
 * @Author: Zhou Hao
 * @Date: 2021-05-06 15:37:46
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-06 15:52:35
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1839 lang=cpp
 *
 * [1839] 所有元音按顺序排布的最长子字符串
 */

// @lc code=start
#include<vector>
#include<string>
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<numeric>
using namespace std;
class Solution {
public:
    int longestBeautifulSubstring(string word) {
        vector<char> window;
        unordered_set<char> count;  //集合存元素
        int res = 0,left =0,right =0;

        while(right<word.size())
        {
            //右滑
            if(window.empty() || word[right]>=window.back())
            {
                window.push_back(word[right]);
                count.insert(word[right]);
                
                if(count.size() == 5)   //如果满足条件,更新答案
                {
                    res = max(res,int(window.size()));
                }
            }
            else    //左滑
            {
                window.clear();     //清空窗口
                count.clear();
                left = right;
                window.push_back(word[left]);
                count.insert(word[left]);
            }
            right++;
        }
        return res;
    }
};
// @lc code=end

