def radix_sort(nums):       O(kn)
    max_num = max(nums)
    it = 0
    while 10 ** it <= max_num:         # k times. max = 999 -> 3
        buckets = [[] for _ in range(10)]
        for var in nums:
            digit = (var // 10 ** it) % 10   # it = 2, 897//100 = 9 9%10 = 9
            buckets[digit].append(var)
        # bucketing done
        nums.clear()
        for buc in buckets:
            nums.extend(buc)
        # put back to nums

        it += 1

import random
nums = list(range(1000))
random.shuffle(nums)
print(nums)
radix_sort(nums)
print(nums)
