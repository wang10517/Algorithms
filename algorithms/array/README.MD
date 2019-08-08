The algorithms related to array usually takes a couple forms as following:
Subarray
Subsequence
Two or more subarray
Two or more subsequence

1. Subarray 
    1.a Length
        1.a.a given a fixed length, get the subarray with sum equal to a certain number 
        1.a.b given a fixed length, get the subarray with sum closest(or equal to ) a certain number
        1.a.b given a fixed length, get the max( or min) sum 
    Solution: see ~/patterns/sliding_window/largest_subarray_sum (no matter if negative numbers are permitted)
    1.b Sum 
        1.b.a given a sum, get the shortest subarray with >= sum 
        1.b.b given a sum, get the longest subarray with <= sum 
        1.b.c given a sum, get the shortest subarray with <= sum (non-trivial only when negative numbers are permitted) 
        1.b.d given a sum, get the longest subarray with >= sum (non-trivial only when negative numbers are permitted)  (unresolved)
        1.b.e given a sum, get the array closest to or equal to a length
    Solution: see ~/patterns/sliding_window/shortest_subarray
    1.c distinct characters
        1.c.a given k characters, find the longest substring with no more than k distinct chars
2. palindrome:
    solution:
        1. compare with the reversed version 
        2. two pointers comparison from both extreme 
        3. use stack with either know length of the list or fast/slow runner pointer
