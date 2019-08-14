/*
 * @lc app=leetcode id=350 lang=cpp
 *
 * [350] Intersection of Two Arrays II
 */
#include <vector>
#include <algorithm>
#include <set>
#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    vector<int> intersect(vector<int> &nums1, vector<int> &nums2)
    {
        // vector<int> longer, shorter;

        // if (nums1.size() > nums2.size())
        // {
        //     longer = nums1;
        //     shorter = nums2;
        // }
        // else
        // {
        //     longer = nums2;
        //     shorter = nums1;
        // }

        vector<int> result;
        multiset<int> ht;

        //Faster, about 8ms as opposed to 12ms
        for (auto it = nums1.begin(); it != nums1.end(); it++)
        {
            ht.insert(*it);
        }

        for (auto it = nums2.begin(); it != nums2.end(); it++)
        {
            if (ht.find(*it) != ht.end())
            {
                result.push_back(*it);
                ht.erase(ht.lower_bound(*it));
            }
        }

        // for_each(nums1.begin(), nums1.end(), [&ht](int ele) {
        //     ht.insert(ele);
        // });
        // for_each(nums2.begin(), nums2.end(), [&result, &ht](int ele) {
        //     if (ht.find(ele) != ht.end())
        //     {
        //         result.push_back(ele);
        //         ht.erase(ht.lower_bound(ele));
        //     }
        // });

        return result;
    }
};
