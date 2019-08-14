/*
 * @lc app=leetcode id=349 lang=cpp
 *
 * [349] Intersection of Two Arrays
 */
#include <unordered_set>;
#include <vector>;
using namespace std;

class Solution
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> ht;
        vector<int> result;
        for (auto i = nums1.begin(); i != nums1.end(); i++)
        {
            ht.insert(*i);
        }

        for (auto j = nums2.begin(); j != nums2.end(); j++)
        {
            if (ht.find(*j) != ht.end())
            {
                result.push_back(*j);
                ht.erase(*j);
            }
        }

        return result;
    }
};
