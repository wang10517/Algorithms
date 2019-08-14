/*
 * @lc app=leetcode id=342 lang=cpp
 *
 * [342] Power of Four
 */
class Solution
{
public:
    bool isPowerOfFour(int num)
    {
        unsigned int n = num;
        return num > 0 && ((n - 1) & n) == 0 && digtiPosition(n) % 2 == 0;
    }

    int digtiPosition(int num)
    {
        int counter = 0;
        while ((num & 1) != 1)
        {
            counter++;
            num = num >> 1;
        }
        return counter;
    }
};

// int main()
// {
//     Solution().isPowerOfFour(16);
// }