def count_sort(nums, max_count=100):           # O(n)
    count = [0 for _ in range(max_count+1)]
    for val in nums:
        count[val] += 1
    nums.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            nums.append(ind)

import random
nums = [random.randint(0,100) for _ in range(1000)]
print(nums)
count_sort(nums)
print(nums)