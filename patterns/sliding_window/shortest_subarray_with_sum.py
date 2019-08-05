import math

"""
    Running time O(N)
    space time O(1)
"""


def shortestSubarray(s, arr):
    start, total, min_len = 0, 0, math.inf
    for i in range(len(arr)):
        total += arr[i]
        while total >= s:
            min_len = min(min_len, i - start + 1)
            total -= arr[start]
            start += 1
    return min_len if min_len != math.inf else 0


def longestSubarray(s, arr):
    start, end, max_len = 0, 0, 0
    total = 0
    while end < len(arr):
        if total > s:
            total -= arr[start]
            start += 1
        while total <= s and end < len(arr):
            max_len = max(max_len, end - start)
            total += arr[end]
            end += 1
    return max_len


def longestSubarrayWithCertainSum(s, arr):
    start, end, max_len, total = 0, 0, 0, 0
    stop = len(arr)
    while end < stop:
        if total > s:
            total -= arr[start]
            start += 1
        while total < s and end < stop:
            total += arr[end]
            end += 1
        if total == s:
            max_len = max(max_len, end-start)
            total -= arr[start]
            start += 1
    return max_len


def shortestSubarryWithLessThanSum(s, arr):
    start, total, min_len = 0, 0, math.inf
    for i in range(len(arr)):
        temp = arr[i] + total
        if temp > arr[i]:
            start = i
            total = arr[i]
        else:
            total = temp
        while total <= s and start <= i:
            min_len = min(i-start + 1, min_len)
            total -= arr[start]
            start += 1
    return min_len

# def longestSubarrayWithMoreThanSum(s, arr):
#     start, end, max_len, total = 0, 0, 0, 0
#     stop = len(arr)
#     pre_info = {
#         "prev_sum" : 0,
#         "start" : None
#     }
#     while end < stop:
#         temp = total + arr[end]
#         if temp < arr[end]:
#             start = end
#             total = arr[end]
#         else:
#             total = temp
#         while total > s:
#             max_len = max(max_len, end - start + 1)
#             if total > pre_info["prev_sum"]:

# https://www.geeksforgeeks.org/largest-subarray-having-sum-greater-than-k/


if __name__ == "__main__":
    print(shortestSubarryWithLessThanSum(-2, [1, -1, -1, 4, 5]))
