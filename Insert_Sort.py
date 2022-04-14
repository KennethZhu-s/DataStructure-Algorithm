def insert_sort(nums):     # O(n^2)
    for i in range(1, len(nums)):   # i -> the card you draw
        tmp = nums[i]
        j = i - 1    # j -> the card in hand
        while j >= 0 and nums[j] > tmp:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp
        #print(nums)
    return nums

nums = [3,4,2,1,5,6,8,7,9]
print(insert_sort(nums))