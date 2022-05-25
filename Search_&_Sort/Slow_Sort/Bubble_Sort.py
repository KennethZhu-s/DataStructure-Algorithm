import random

def bubble_sort(nums):      # O(n^2)
    for i in range(len(nums)-1):   # ith times
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]




##### Optimization
def bubble_sort(nums):
    for i in range(len(nums)-1):   # ith times
        exchange = False  # improve step
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                exchange = True    # if it is still false, end the loop
        if not exchange:
            return nums

nums = [random.randint(0, 10000) for i in range(1000)]
print(nums)

bubble_sort(nums)
print(nums)