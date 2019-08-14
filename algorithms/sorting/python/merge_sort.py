def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = (start+end)//2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, mid, end)
    return


def merge(arr, start, middle, end):
    buffer_low = arr[start:middle+1].copy()
    buffer_high = arr[middle+1: end+1].copy()
    i, l, h = 0, 0, 0
    stop_high = len(buffer_high)
    stop_low = len(buffer_low)
    while l < stop_low and h < stop_high:
        if buffer_high[h] < buffer_low[l]:
            arr[start+i] = buffer_high[h]
            h += 1
        else:
            arr[start+i] = buffer_low[l]
            l += 1
        i += 1
    while l < stop_low:
        arr[start+i] = buffer_low[l]
        l += 1
        i += 1

    while l < stop_high:
        arr[start+i] = buffer_high[l]
        h += 1
        i += 1

    return


a = [45, 123, 87, 0, 93, -1]
merge_sort(a, 0, 5)
a
