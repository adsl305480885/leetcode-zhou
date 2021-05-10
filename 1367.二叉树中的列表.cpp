/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 21:37:37
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-07 21:58:01
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1367 lang=cpp
 *
 * [1367] 二叉树中的列表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    //bfs找到起点
    //dfs往下匹配

    //前序遍历
    bool dfs(ListNode* head, TreeNode* root) {
    if (head == nullptr) return true;
    if (root == nullptr) return false;
    if (root->val != head->val) return false;
    return dfs(head->next, root->left) || dfs(head->next, root->right);
    }

    
    bool isSubPath(ListNode* head, TreeNode* root) {
        queue<TreeNode*> que;
        que.push(root);

        while (!que.empty()) {
            auto q = que.front();
            que.pop();
            if (q == nullptr) continue;

            if (q->val == head->val) {
                if (dfs(head, q)) return true;
            }
            que.push(q->left);
            que.push(q->right);
        }
        return false;
    }
};
// @lc code=end

