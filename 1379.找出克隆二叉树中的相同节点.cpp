/*
 * @Author: Zhou Hao
 * @Date: 2021-05-10 22:05:19
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-10 22:12:07
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1379 lang=cpp
 *
 * [1379] 找出克隆二叉树中的相同节点
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
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

    //前序遍历
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        
        if(original == target) return cloned;
        if(original == NULL || cloned == NULL) return NULL;

        TreeNode *left = getTargetCopy(original->left,cloned->left,target);
        TreeNode *right = getTargetCopy(original->right,cloned->right,target);

        return left == NULL? right:left;    //哪个不为空就返回哪个
    }
};
// @lc code=end

