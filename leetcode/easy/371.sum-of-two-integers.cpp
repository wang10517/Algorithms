/*
 * @lc app=leetcode id=371 lang=cpp
 *
 * [371] Sum of Two Integers
 */
class Solution
{
public:
    int getSum(int a, int b)
    {
        
        unsigned int carry;

        while (b != 0)

        {

            carry = a & b;

            a = a ^ b;

            b = carry << 1;
        }

        return a;
    }
};
