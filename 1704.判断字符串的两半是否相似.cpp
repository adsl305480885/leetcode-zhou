/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 15:07:51
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 15:43:16
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1704 lang=cpp
 *
 * [1704] 判断字符串的两半是否相似
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
    // bool halvesAreAlike(string s) {
    //     unordered_set<char> uset{ 'a','e','i','o','u','A','E','I','O','U'};

    //     string left=s.substr(0,s.size()/2),right = s.substr(s.size()/2,s.size()/2);

    //     int left_num=0,right_num = 0;
    //     for(int i=0;i<s.size()/2;i++)
    //     {
    //         if(uset.find(left[i]) != uset.end())   left_num+=1;
    //         if(uset.find(right[i]) != uset.end())   right_num+=1;
    //     }
    
    //     return left_num == right_num;
    // }
    
    
    bool halvesAreAlike(string s) {
        unordered_set<char> uset{ 'a','e','i','o','u','A','E','I','O','U'};

        int length = s.size();
        int left_num=0,right_num = 0;
        for(int i =0;i<length/2;i++)
        {	
            if(uset.find(s[i])!=uset.end()) left_num++;
            if(uset.find(s[length-1-i])!=uset.end()) right_num++;
        }
        
        return left_num == right_num;

    }
};
// @lc code=end

