def pair_with_targetsum(arr, target_sum):
    if not arr:
        return -1 
    spt, bpt = 0, len(arr) -1
    while spt != bpt:
        cur_sum = arr[spt] + arr[bpt]
        if cur_sum > target_sum:
            bpt -= 1
        elif cur_sum < target_sum:
            spt += 1
        else:
            return [spt,bpt]
    return [-1, -1]

# hashTable solution
def pair_with_targetsum(arr, target_sum):
  nums = {}  # to store numbers and their indices
  for i, num in enumerate(arr):
    if target_sum - num in nums:
      return [nums[target_sum - num], i]
    else:
      nums[arr[i]] = i
  return [-1, -1]

