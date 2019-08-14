/*
 * @lc app=leetcode id=389 lang=cpp
 *
 * [389] Find the Difference
 */
#include <unordered_map>
using namespace std;
class Solution
{
public:
    char findTheDifference(string s, string t)
    {
        unordered_map<char, int> ht;
        for (auto chr : s)
        {
            if (ht.find(chr) == ht.end())
            {
                ht[chr] = 1;
            }
            else
            {
                ht[chr] += 1;
            }
        }
        for (auto chr : t)
        {
            if (ht.find(chr) == ht.end())
            {
                return chr;
            }
            else
            {
                ht[chr] -= 1;
                if (ht[chr] == 0)
                {
                    ht.erase(chr);
                }
            }
        }
        char val = 'l';
        return val;
    }
};
