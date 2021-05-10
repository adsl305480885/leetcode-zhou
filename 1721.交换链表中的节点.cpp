/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 21:25:37
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-10 15:37:28
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=1721 lang=cpp
 *
 * [1721] 交换链表中的节点
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
    //快慢指针
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* fast = head;
        while (k-1!=0)
        {
            fast = fast->next;
            k--;
        }
        ListNode* left_node = fast;     //正数第k个

        ListNode* slow = head;
        while(fast->next)
        {
            fast = fast->next;
            slow = slow->next;
        }
        ListNode* right_node = slow;        //倒数第k个
        
        //交换
        int temp = right_node->val;
        right_node->val = left_node->val;
        left_node->val = temp;
        return head;
    }
};
// @lc code=end

