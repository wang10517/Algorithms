/*
 * @lc app=leetcode id=392 lang=cpp
 *
 * [392] Is Subsequence
 */
class Solution {
public:
    bool isSubsequence(string s, string t) {
        std::string::iterator it = t.begin();
        for (auto chr : s){
            while(it != t.end() && *it != chr){
                it++; 
            }
            if (it == t.end()){
                return false;
            }else{
                it++;
            }
        }
        return true;
    }
};

