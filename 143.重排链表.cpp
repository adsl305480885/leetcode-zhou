/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 16:28:24
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-07 16:39:56
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=143 lang=cpp
 *
 * [143] 重排链表
 */

// @lc code=start


// struct ListNode {
//     int val;
//     ListNode *next;
//     ListNode() : val(0), next(nullptr) {}
//     ListNode(int x) : val(x), next(nullptr) {}
//     ListNode(int x, ListNode *next) : val(x), next(next) {}
// };


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
    
    void reorderList(ListNode* head) {
        if (head == nullptr) return ;
        //空间换时间
        vector<ListNode*> v;
        ListNode *p = head;
        while(p) 
            v.push_back(p),
            p = p->next;
        

        //双指针遍历容器交叉重排
        int left = 0, right = v.size() - 1;
        while(left < right) {
            v[left]->next = v[right];
            v[right]->next = v[left+1];
            left++;
            right--;
        }
        v[left]->next = NULL;       //别忘记置为空否则是循环的
    }
};
// @lc code=end

