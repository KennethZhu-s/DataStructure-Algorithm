def partition(nums, left, right):
    tmp = nums[left]
    while left < right:
        while left < right and nums[right] >= tmp:  #search digit less than tmp from the right
            right -= 1     # move 1 step to the left
        nums[left] = nums[right]    # move the digit on the right to the blank place on the left
        while left < right and nums[left] <= tmp:
            left += 1
        nums[right] = nums[left]   # move the digit on the left to the blank place on the right
    nums[left] = tmp      # put tmp back to nums
    return left

def quick_sort(nums, left, right):    # O(nlogn)    logn layers
    if left < right:    # nums has at least 2 elements
        mid = partition(nums, left, right)
        quick_sort(nums, left, mid - 1)
        quick_sort(nums, mid + 1, right)


nums = [5,7,4,6,3,1,2,9,8]
print(nums)
quick_sort(nums, 0, len(nums) - 1)
print(nums)
