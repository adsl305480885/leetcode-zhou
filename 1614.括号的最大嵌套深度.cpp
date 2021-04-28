/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 13:13:57
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 13:18:08
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1614 lang=cpp
 *
 * [1614] 括号的最大嵌套深度
 */

// @lc code=start

#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
public:
    int maxDepth(string s) {
        int cur = 0 , maxdeep = 0;

        for(auto c:s)
        {
            if(c=='(') cur ++;
            else if (c==')') cur--;
            
            if(cur>maxdeep) maxdeep = cur;
        }

        return maxdeep;
    }
};
// @lc code=end

