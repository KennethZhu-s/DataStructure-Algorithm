import heapq
import random

nums = list(range(10))
random.shuffle(nums)
print(nums)

heapq.heapify(nums)
print(nums)

n = len(nums)
for i in range(n):
    print(heapq.heappop(nums), end = ',')
