def insertMap(hashMap, char):
    if char in hashMap:
        hashMap[char] += 1
    else:
        hashMap[char] = 1


def longest_substring_with_k_distinct(string, k):
    start, end, maxLen = 0, 0, 0
    chars = {}
    stop = len(string)
    while end < stop:
        if len(chars) < k:
            manLen = max(maxLen, len(chars))
            insertMap(chars, string[end:end+1])
            end += 1
        elif len(chars) > k:
            chars[string[start:start+1]] -= 1
            start += 1
        else:
            while len(chars) == k:
                manLen = max(maxLen, len(chars))
                if end >= stop:
                    break
                insertMap(chars, string[end:end+1])
                end += 1
    return maxLen


def longest_substring_with_k_distinct(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end-window_start + 1)
    return max_length

# use case
# Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.


def fruits_into_baskets(fruits):
    start, end, maxLen = 0, 0, 0
    cur_fruits = {}
    for i in range(len(fruits)):
        insertMap(cur_fruits, fruits[i])
        while len(cur_fruits) > 2:
            cur_fruit = fruits[start]
            cur_fruits[cur_fruit] -= 1
            if cur_fruits[cur_fruit] == 0:
                del cur_fruits[cur_fruit]
            start -= 1
        maxLen = max(maxLen, i - start + 1)


def non_repeat_substring(string):
    if not string:
        return 0
    start, end, maxLen = 0, 0, 0
    chars = set()
    for i in range(len(string)):
        cur_char = string[i]
        while cur_char in chars:
            chars.remove(string[start])
            start += 1
        chars.add(cur_char)
        maxLen = max(maxLen, len(chars))
    return maxLen

# with one replacement change of k chars of the same one
def length_of_longest_substring(str, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_frequency) > 2:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        for i in char_frequency:
            if char_frequency[i] == k:
                max_length = max(max_length, window_end-window_start + 1)

    return max_length

# with all zeros and ones
def length_of_longest_substring(arr, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while char_frequency[0] > k:
            left_char = arr[window_start]
            char_frequency[left_char] -= 1
            window_start += 1  # shrink the window
    
        max_length = max(max_length, window_end-window_start + 1)

    return max_length
