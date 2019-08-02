import math


def remove_duplicates(arr):
    pta, ptb = 0, 1
    newLen = 0
    while pta < len(arr) and ptb < len(arr):
        if arr[pta] == arr[ptb]:
            newLen += 1
        if pta > ptb:
            ptb = pta + 1
        else:
            pta = ptb + 1
    return len(arr) - newLen


def remove_duplicates(arr):
    # index of the next non-duplicate element
    # assume the array was sorted
    next_non_duplicate = 1

    i = 1
    while(i < len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


# def remove_element(arr, key):
#   nextElement = 0  # index of the next element which is not 'key'
#   for i in range(len(arr)):
#     if arr[i] != key:
#       arr[nextElement] = arr[i]
#       nextElement += 1

#   return nextElement

def search_triplets(arr):
    triplets = []
    # TODO: Write your code here
    return triplets


def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
        search_pair(arr, -arr[i], i+1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # skip same element to avoid duplicate triplets
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # skip same element to avoid duplicate triplets
        elif target_sum > current_sum:
            left += 1  # we need a pair with a bigger sum
        else:
            right -= 1  # we need a pair with a smaller sum


# sliding window approach
# just realize that a triple could be non continuous


def triplet_sum_close_to_target(arr, target_sum):
    start, total = 0, 0
    minDiff = math.inf
    triplet = []
    for i in range(len(arr)):
        total += arr[i]
        if i >= 2:
            if abs(total - target_sum) < minDiff:
                minDiff = abs(total - target_sum)
                triplet = arr[start: i+1]
            total -= arr[start]
            start += 1
    return triplet


def triplet_sum_close_to_target(arr, target_sum):
    arr.sort()
    minDiff = math.inf
    right = len(arr) - 1
    triplet = []
    for i in range(len(arr)):
        rest_sum = target_sum - arr[i]
        left = i + 1
        while left < right:
            cur_sum = arr[left] + arr[right]
            if cur_sum == rest_sum:
                return [arr[i], arr[left], arr[right]]

            if abs(cur_sum - rest_sum) < minDiff:
                minDiff = abs(cur_sum - rest_sum)
                triplet = [arr[i], arr[left], arr[right]]

            if cur_sum > rest_sum:
                right -= 1
            else:
                left += 1

    return triplet
