from functools import cmp_to_key

nums = [32, 94, 128, 1286, 6, 71]

def xy_cmp(x, y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

def number_join(nums):
    nums = list(map(str, nums))    # convert to string
    nums.sort(key=cmp_to_key(xy_cmp))
    return "".join(nums)

print(number_join(nums))

    