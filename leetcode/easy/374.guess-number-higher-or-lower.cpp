// /*
//  * @lc app=leetcode id=374 lang=cpp
//  *
//  * [374] Guess Number Higher or Lower
//  */
// // Forward declaration of guess API.
// // @param num, your guess
// // @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
// #include <iostream>
// int guess(int num);

// class Solution
// {
// public:
//     int guessNumber(int n)
//     {
//         int l = 1, h = n;
//         while (l <= h)
//         {
//             int md = (l + h) / 2;
//             guess(md);
//             int response;
//             std::cin >> response;
//             std::cout << md;
//             std::cout << response;
//             if (response == 0)
//             {
//                 return md + 1;
//             }
//             else if (response == -1)
//             {
//                 l = md + 1;
//             }
//             else
//             {
//                 h = md - 1;
//             }
//         }
//         return 0;
//     }
// };

// Something wrong with the api, easy binary search should do
