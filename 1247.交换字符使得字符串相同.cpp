/*
 * @Author: Zhou Hao
 * @Date: 2021-05-10 21:52:08
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-10 22:02:56
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1247 lang=cpp
 *
 * [1247] 交换字符使得字符串相同
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
    int minimumSwap(string s1, string s2) {
        int count = 0;
        int neg = 0, pos = 0;  //1:pos,  0:neg
        for(int i = 0; i <s1.size();i++)
        {
            if(s1[i]-s2[i] == 1) pos++;
            else if(s1[i]-s2[i] == -1) neg++;
        }

        if(neg %2 != pos %2) return -1;//两俩抵消后剩下的数量不一样
        return pos/2+neg/2+ neg%2 + pos%2;

    }
};
// @lc code=end

