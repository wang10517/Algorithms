/*
 * @lc app=leetcode id=303 lang=cpp
 *
 * [303] Range Sum Query - Immutable
 */
class NumArray
{
public:
    NumArray(vector<int> &nums) : nums{nums} {}

    int sumRange(int i, int j)
    {
        int sum = 0;
        for (int idx = i ; idx <= j ; idx++){
            sum += nums[idx];
        }
        return sum;
    }

private:
    vector<int> &nums;
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
