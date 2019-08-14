/*
 * @lc app=leetcode id=367 lang=cpp
 *
 * [367] Valid Perfect Square
 */
#include <cmath>
class Solution
{
public:
    bool isPerfectSquare(int num)
    {
        int l = 0, h = num;
        while (l <= h)
        {
            int md = (l + h) / 2;
            long long square = pow(md, 2);
            if (square == num)
            {
                return true;
            }
            else if (square > num)
            {
                h = md - 1;
            }
            else
            {
                l = md + 1;
            }
        }
        return false;
    }
};
