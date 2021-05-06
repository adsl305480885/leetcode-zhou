/*
 * @Author: Zhou Hao
 * @Date: 2021-05-06 15:11:00
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-06 15:27:23
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1423 lang=cpp
 *
 * [1423] 可获得的最大点数
 */

// @lc code=start
#include<vector>
#include<string>
#include<iostream>
#include<unordered_map>
#include<unordered_set>
#include<algorithm>
#include<numeric>
using namespace std;
class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {

        int windowSize = cardPoints.size() - k;
        
        //TODO  accumulate函数
        int sum = accumulate(cardPoints.begin(),cardPoints.begin()+windowSize,0);
        int minSum = sum;
        
        for(int i = windowSize;i<cardPoints.size();++i)
        {   //滑动窗口,右边加一个,左边减一个
            sum += cardPoints[i]-cardPoints[i-windowSize];
            minSum = min(minSum,sum);
        }

        return accumulate(cardPoints.begin(),cardPoints.end(),0) - minSum;
    }
};
// @lc code=end

