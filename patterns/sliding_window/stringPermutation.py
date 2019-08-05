import math
# and why match == len(pattern), shouldn't it be match == set(pattern) or len(chars)


def find_string_anagrams(string, pattern):
    result_indexes = []
    start, match = 0, 0
    chars = {}
    for char in pattern:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] == 1

    for i in range(len(string)):
        if string[i] in chars:
            chars[string[i]] -= 1
            if chars[string[i]] == 0:
                match += 1

        if match == len(chars):
            result_indexes.append(start)

        if i >= len(pattern) - 1:
            start_char = string[start]
            if start_char in chars:
                if chars[start_char] == 0:
                    match -= 1
                chars[start_char] += 1
            start += 1

    return result_indexes


def find_permutation(string, pattern):
    start, match = 0, 0
    chars = {}
    minLen = math.inf
    min_start, min_end = math.inf, math.inf
    for char in pattern:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

    for i in range(len(string)):
        if string[i] in chars:
            chars[string[i]] -= 1
            if chars[string[i]] == 0:
                match += 1

        while match == len(chars):
            if minLen > i - start + 1:
                minLen = i - start + 1
                min_start = start
                min_end = i
            start_char = string[start]
            if start_char in chars:
                if chars[start_char] == 0:
                    match -= 1
                chars[start_char] += 1
            start += 1

    return string[min_start: min_end+1] if min_start < len(string) else None


def toMap(string):
    chars = {}
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def find_word_concatenation(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(str) - words_count * word_length)+1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = str[next_word_index: next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == words_count:  # Store index if we have found all the words
                result_indices.append(i)

    return result_indices
