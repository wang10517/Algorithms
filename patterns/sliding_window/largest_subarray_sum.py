"""
    running time O(n) with space O(1)
"""

"""
    Takeaway:
        1. when checking special condition, put the checking at the later part to avoid the 
            edge case of last element not checked
        2. beginning index = cur_end - total_length + 1 
"""

def maxSubArray(arr, k):
    total = 0
    max_sum = 0
    for i in range(len(arr)):
        total = total + arr[i]

        if i >= k - 1:
            max_sum = max(total,max_sum)
            total = total - arr[i - k + 1]
    return max_sum




