def binarySearch(array, target):
    if not array:
        return -1

    l, h = 0, len(array)-1
    while l <= h:
        mid = (l + h)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == "__main__":
    print(binarySearch([1, 2, 3, 4, 5], 4))
    print(binarySearch([1, 2, 3, 4, 5], 5))
    print(binarySearch([1, 2, 3, 4, 5], 1))
