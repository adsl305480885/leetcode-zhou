/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 10:41:10
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-07 11:29:08
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=111 lang=cpp
 *
 * [111] 二叉树的最小深度
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

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
    int minDepth(TreeNode* root) {
        if (root) {
            int height = 1, cnt = 0;
            queue<TreeNode*> que;       //用队列储存每一层的所有节点
            que.push(root);
            while (!que.empty()) 
            {
                int sz = que.size();
                for (int i=0; i<sz; ++i)        //遍历这一层的元素
                {
                    root = que.front();     //这里不能直接pop
                    if (!root->left && !root->right) return height; //判断叶子节点
                    if (root->left)  que.push(root->left);   //队列中加入下一层的元素
                    if (root->right)  que.push(root->right);
                    que.pop();      //C++队列pop不返回元素
                }
                ++height;
            }
        }
        return 0;
    }
};
// @lc code=end

