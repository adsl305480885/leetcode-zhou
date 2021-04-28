/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 11:20:54
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 11:28:32
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=893 lang=cpp
 *
 * [893] 特殊等价字符串组
 */

// @lc code=start
#include<algorithm>
#include<string>
using namespace std;
#include<map>
#include<iostream>
#include <unordered_set>
#include<vector>

class Solution {
public:
    int numSpecialEquivGroups(vector<string>& A) {

        unordered_set<string> set_;
        for(int i =0;i<A.size();i++)
        {
            string ji = "",ou = "";
            for(int j=0;j<A[i].size();j++)
            {
                if(j %2==0) ji+=A[i][j];
                else ou += A[i][j];
            }
            sort(ji.begin(),ji.end());
            sort(ou.begin(),ou.end());
        
            set_.insert(ji+ou);
        }
        
        return set_.size();
        



    }
};
// @lc code=end

