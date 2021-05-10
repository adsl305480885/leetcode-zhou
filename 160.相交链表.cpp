/*
 * @Author: Zhou Hao
 * @Date: 2021-05-07 16:51:43
 * @LastEditors: Zhou Hao
 * @LastEditTime: 2021-05-07 21:20:31
 * @Description: file content
 * @E-mail: 2294776770@qq.com
 */
/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
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

    //双指针,一个链表一个指针
    // ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    //     auto pa = headA,pb = headB;
    //     while (pa!=pb)
    //     {
    //         pa = (pa!=nullptr? pa->next:headB);
    //         pb = (pb != nullptr ? pb->next:headA);
    //     }
    //     return pa;
    // }



    //哈希表存链表A的地址/引用
    // ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
    //     unordered_map<ListNode*,int> map_;

    //     while(headA)
    //     {
    //         map_[headA]++;
    //         headA = headA->next;
    //     }
    //     while(headB)
    //     {
    //         if(map_[headB]) return headB;
    //         headB = headB->next;
    //     }
    //     return NULL;
    // }


    //让长链表先走几步
    // ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        //先计算两个链表的长度
    //     int length_A =0,length_B = 0;
    //     auto curA = headA, curB= headB;
    //     while (curA)
    //     {
    //         length_A++;
    //         curA = curA->next;
    //     }
    //     while(curB)
    //     {
    //         length_B++;
    //         curB = curB->next;
    //     }

    //     curA = headA, curB= headB;
    //     if(length_A >= length_B)
    //     {
    //         int step = length_A - length_B; //多出来的几个节点
    //         while(step)
    //             curA = curA->next,step--;   //长的链表多走几步
    //     }
    //     else
    //     {
    //         int step = length_B - length_A;
    //         while (step)
    //             curB = curB->next,step--;
    //     }

    //     while (curB)        //再开始同时走
    //         {
    //             if(curA == curB) return curA;
    //             curA = curA->next;
    //             curB = curB->next;
    //         }

    //     return NULL;
    // }


    //暴力
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        auto pA = headA,pB = headB;
        while(pA)
        {
            while(pB)
            {
                if(pA == pB) return pA;
                pB = pB->next;
            }
            pB = headB;
            pA = pA->next;
        }
        return NULL;
    }
};
// @lc code=end

