def insert_sort_gap(nums, gap):     # O(n^2)
    for i in range(gap, len(nums)):   # i -> the card you draw
        tmp = nums[i]
        j = i - gap    # j -> the card in hand
        while j >= 0 and nums[j] > tmp:
            nums[j+gap] = nums[j]
            j -= gap
        nums[j+gap] = tmp

def shell_sort(nums):
    d = len(nums) // 2
    while d >= 1:
        insert_sort_gap(nums, d)
        d //= 2

nums = list(range(100))
import random
random.shuffle(nums)
print(nums)
shell_sort(nums)
print(nums)