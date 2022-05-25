def select_sort_simple(nums):   # O(n^2) not O(n) or O(n^3)
    nums_new = []         # require more space
    for i in range(len(nums)):  # O(n)
        min_val = min(nums)       # O(n)
        nums_new.append(min_val)
        nums.remove(min_val)    # O(n)
    return nums_new

def select_sort(nums):
    for i in range(len(nums)-1):   # ith times
        min_loc = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_loc]:
                min_loc = j
        if min_loc != i:
            nums[i], nums[min_loc] = nums[min_loc], nums[i]
        print(nums)
    return nums

nums = [3,4,2,1,5,6,8,7,9]
print(select_sort(nums))