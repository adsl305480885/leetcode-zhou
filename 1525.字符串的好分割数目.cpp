/*
 * @lc app=leetcode.cn id=1525 lang=cpp
 *
 * [1525] 字符串的好分割数目
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

    //hash
    int numSplits(string s) {
        unordered_map<char,int> total,cur_left;
        for(auto x:s) total[x]++;
        int res = 0,count = total.size();

        for(auto c:s)
        {
            total[c]--,cur_left[c]++;
            if(total[c] == 0) count--;
            if(count == cur_left.size()) res++; //左右字典长度相等，就是一个好分割

        }

        return res;



    }
};
// @lc code=end

