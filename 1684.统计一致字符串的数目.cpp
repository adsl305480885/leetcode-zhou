/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 15:46:48
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 16:10:58
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1684 lang=cpp
 *
 * [1684] 统计一致字符串的数目
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
    int countConsistentStrings(string allowed, vector<string>& words) {
        int res = 0;
        for(int i =0;i<words.size();i++)
        {
            res++;
            
            for(int j =0;j<words[i].size();j++)
            {
                if((long long)allowed.find(words[i][j]) == -1) 
                {	
                    res--;
                    break;
                }
            }
        }
        
        return res;




    }
};
// @lc code=end

