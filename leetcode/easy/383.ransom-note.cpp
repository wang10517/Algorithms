/*
 * @lc app=leetcode id=383 lang=cpp
 *
 * [383] Ransom Note
 */
// seems that hashmap is way faster than hashset despite equal algorithm abstractly
#include <set>
using namespace std;
class Solution
{
public:
    bool canConstruct(string ransomNote, string magazine)
    {
        unordered_multiset<char> letters;
        for (auto it = magazine.begin(); it != magazine.end(); it++)
        {
            letters.insert(*it);
        }

        for (auto it = ransomNote.begin(); it != ransomNote.end(); it++)
        {
            auto idx = letters.find(*it);
            if (idx != letters.end())
            {
                letters.erase((idx));
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};
