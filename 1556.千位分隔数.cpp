/*
 * @Author: Zhou Hao
 * @Date: 2021-04-28 14:02:15
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-28 14:42:06
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1556 lang=cpp
 *
 * [1556] 千位分隔数
 */

// @lc code=start
#include<string>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
class Solution {
public:
    //额外空间
    // string thousandSeparator(int n) {
    //     string num = to_string(n);
    //     string denum = num;
    //     reverse(denum.begin(),denum.end());
        
        
    //     string res;
    //     for(int i =0;i<denum.size();i++)
    //     {
    //         res += denum[i];
    //         if((i+1)%3==0 && i!=denum.size()-1){
    //             res += '.';
    //         }
    //     }
    //     reverse(res.begin(),res.end());
    //     return res;
    // }      

    //原地
    string thousandSeparator(int n) {
        string num = to_string(n);
        int index = num.size()-1;
        int temp = 0;       //记录已经走过的数字个数

        while(index>0)  //从后往前遍历
        {
            if('0'<num[index]<'9')temp++;
            if((temp%3) == 0){
                num.insert(index,".");
                temp =0;
            }
            index--;
        }
        return num;

    } 
};
// @lc code=end

