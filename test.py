def bucket_sort(nums, n=100, max_num = 10000):
    buckets = [[] for _ in range(n)]
    for var in nums:
        i = min((var // (max_num // n)), n-1)
        buckets[i].append(var)

        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_num = []
    for buc in buckets:
        sorted_num.extend(buc)
    return sorted_num


#nums = [9,4,2,1,5,6,8,7,3]
#print(shell_sort(nums), 'result')

import random
nums = [random.randint(0,100000000) for _ in range(100)]
#print(nums)
nums = bucket_sort(nums)
print(nums)