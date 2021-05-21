/*
 * @Author: Zhou Hao
 * @Date: 2021-05-18 21:22:08
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-18 21:56:00
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=470 lang=cpp
 *
 * [470] 用 Rand7() 实现 Rand10()
 */

// @lc code=start
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    //若rand_n()能等概率生成1到n的随机整数，则有(rand_n() - 1) * n + rand_n()能
    //等概率生成1到n * n的随机整数。




    int rand10() {
        int i = (rand7()-1)*7 + rand7();
        while(i>40)
        {
            i = (rand7()-1)*7 + rand7();
        }
        return i%10 + 1;
    }




    //方法二：拒绝采样法
};
// @lc code=end

