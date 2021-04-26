/*
 * @Author: Zhou Hao
 * @Date: 2021-04-22 16:32:30
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-23 09:28:32
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=383 lang=cpp
 *
 * [383] 赎金信
 */

// @lc code=start
#include<string>
#include<map>
#include<unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char,int> hashmap;
        for (char m:magazine)       //遍历字符串
        {
            hashmap[m] ++;
        }


        for(int i =0;i<ransomNote.size();i++)
        {
            hashmap[ransomNote[i]]--;
            if(hashmap[ransomNote[i]] <0)
            {
                return false;
            }
        }

            
        return true;

    }
};
// @lc code=end

