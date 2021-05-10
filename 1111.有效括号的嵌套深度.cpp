/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 15:14:40
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-07 15:36:43
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1111 lang=cpp
 *
 * [1111] 有效括号的嵌套深度
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
    // vector<int> maxDepthAfterSplit(string seq) {
    //     int depth = 0;
    //     vector<int> ans;
    //     for(auto c:seq)
    //     {
    //         if(c == '(')
    //         {
    //             ++depth;
    //             ans.push_back(depth%2);
    //         }
    //         else
    //         {
    //             // depth--;
    //             ans.push_back(depth%2);
    //             --depth;
    //         }
    //     }
        
    //     return ans;
    // }


    vector<int> maxDepthAfterSplit(string seq) {
        int d = 0;
        vector<int> ans;
        for (char& c : seq)
            if (c == '(') {
                
                ans.push_back(d);
                d++;
            }
            else {
                d--;
                ans.push_back(d);
                // d--;
            }
        return ans;
    }
};
// @lc code=end

