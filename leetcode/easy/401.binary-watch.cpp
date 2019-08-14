/*
 * @lc app=leetcode id=401 lang=cpp
 *
 * [401] Binary Watch
 */
#include <cmath>
#include <string>
#include <vector>
using namespace std;
class Solution
{
public:
    vector<string> readBinaryWatch(int num)
    {
        vector<int> pool(num, 1);
        for (auto i = 0; i < 10 - num; i++)
        {
            pool.push_back(0);
        }

        vector<string> result;
        vector<int> memo(10, 0);
        getCombo(result, memo, pool, 10, 0, 0, num - 1);
        return result;
    }

    // using coroutine ?
    // generating all combo in n(n C k ) time
    void getCombo(vector<string> &result, vector<int> &memo, vector<int> pool, int n, int k, int start, int maxK)
    {
        if (k > maxK)
        {
            vector<int> hours(memo.begin(), memo.begin() + 4);
            vector<int> mins(memo.begin() + 4, memo.end());
            string time = parseDigits(hours, mins);
            // cout << "before push";
            result.push_back(time);
            // cout << "pushed " + time;
            return;
        }

        for (auto i = start; i < n; i++)
        {
            memo[k] = pool[i];
            getCombo(result, memo, pool, n, k + 1, start + 1, maxK);
        }
    }

    string parseDigits(vector<int> hours, vector<int> mins)
    {
        int hour = 0, min = 0;
        int radix = 0;
        for (auto it = hours.end() - 1; it != hours.begin() - 1; it--)
        {
            hour += *it * pow(2, radix);
            radix++;
        }
        radix = 0;
        for (auto it = mins.end() - 1; it != mins.begin() - 1; it--)
        {
            min += *it * pow(2, radix);
        }
        string min_str = to_string(min);
        if (min_str.size() == 1)
        {
            min_str = "0" + min_str;
        }
        return to_string(hour) + ":" + min_str;
    }
};
