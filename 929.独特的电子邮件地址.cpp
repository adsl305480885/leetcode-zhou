/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 11:28:52
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 12:07:44
 * @Description: file contenti
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=929 lang=cpp
 *
 * [929] 独特的电子邮件地址
 */

// @lc code=start
#include<string>
#include<vector>
#include<unordered_map>
#include<iostream>
#include<unordered_set>
using namespace std;



class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        unordered_set<string> set_;
        
        for(auto email:emails)
        {   
            string name,address;
            int pos = email.find("@");
            address = email.substr(pos,email.size()-pos-1);
            for(int i = 0; i< pos;i++)
            {   
                if(email[i] == '+') break;

                if(email[i]!='.') name += email[i];
            }
            set_.insert(name+address);
        }
        return set_.size();
    }
};
// @lc code=end

