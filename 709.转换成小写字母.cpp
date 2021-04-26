/*
 * @Author: Zhou Hao
 * @Date: 2021-04-26 10:01:31
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-04-26 10:05:42
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=709 lang=cpp
 *
 * [709] 转换成小写字母
 */
using namespace std;
#include <string>
// @lc code=start
class Solution {
public:
    string toLowerCase(string str) {
        for(int i =0;i<str.size();i++)
        {
            if(str[i]>='A'&&str[i]<='Z')
            {
                str[i]+=32;
            }

            
        }
        return str;
    }
};
// @lc code=end

