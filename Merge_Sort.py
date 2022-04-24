def merge(nums, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:    # make sure have digits on both sides
        if nums[i] < nums[j]:
            ltmp.append(nums[i])
            i += 1
        else:
            ltmp.append(nums[j])
            j += 1
        # after this, there must be one side out of digits!!!
    while i <= mid:
        ltmp.append(nums[i])
        i += 1
    while j <= high:
        ltmp.append(nums[j])
        j += 1
    nums[low:high+1] = ltmp

def merge_sort(nums, low, high):
    if low < high:   # at least 2 elements, recursive
        mid = (low + high) // 2
        merge_sort(nums, low, mid)
        merge_sort(nums, mid+1, high)
        merge(nums, low, mid, high)

nums = list(range(100))
import random
random.shuffle(nums)
print(nums)
merge_sort(nums, 0, len(nums)-1)
print(nums)

