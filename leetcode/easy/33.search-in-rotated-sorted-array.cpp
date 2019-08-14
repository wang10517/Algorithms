/*
 * @lc app=leetcode id=33 lang=cpp
 *
 * [33] Search in Rotated Sorted Array
 */
#include <vector>
using std::vector;

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int start = 0, end = nums.size() - 1;
        while (start <= end)
        {
            int mid_idx = (start + end) / 2;
            int mid_val = nums[mid_idx];
            if (mid_val == target)
            {
                return mid_idx;
            }
            else
            {
                if (nums[start] <= mid_val)
                {
                    if (target >= nums[start] && target <= mid_val)
                    {
                        end = mid_idx - 1;
                    }
                    else
                    {
                        start = mid_idx + 1;
                    }
                }
                else
                {
                    if (target >= mid_val && target <= nums[end])
                    {
                        start = mid_idx + 1;
                    }
                    else
                    {
                        end = mid_idx - 1;
                    }
                }
            }
        }
        return -1;
    }
};
