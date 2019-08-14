/*
 * @lc app=leetcode id=344 lang=cpp
 *
 * [344] Reverse String
 */
class Solution
{
public:
    void reverseString(vector<char> &s)
    {
        int length = s.size();
        for (int i = 0; i < length / 2; i++)
        {
            swap(s, i, length - i - 1);
        }
    }

    void swap(vector<char> &s, int i, int j)
    {
        int temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
};
