def sift(nums, low, high):
    """
    :param nums: list
    :param low: heap's root position
    :param high: heap's last position
    :return:
    """
    i = low         # i starts to point to root node
    j = 2 * i + 1     # j is left child of i
    tmp = nums[low]    # store the top of heap
    while j <= high:     # as long as j has number
        if j+1 <= high and nums[j+1] > nums[j]:   # if right child exists and right child is greater
            j = j + 1     # j point to right child
        if nums[j] > tmp:
            nums[i] = nums[j]
            i = j              # go to the next layer
            j = 2 * i + 1
        else:            # tmp greater
            nums[i] = tmp     # put tmp on one of the node
            break
    else:
        nums[i] = tmp    # put tmp on leave


def heap_sort(nums):    # O(nlogn)
    n = len(nums)
    for i in range((n-2)//2, -1, -1):     # father node = (i - 1) // 2, now i = n -1
        # i = the position of the root of the part that needs to be sifted
        sift(nums, i, n-1)
        # done building heap!
    for i in range(n-1, -1, -1):   # i always points the last element of heap
        nums[0], nums[i] = nums[i], nums[0]
        sift(nums, 0, i-1)       # i -1 is new high


nums = [i for i in range(100)]
import random
random.shuffle(nums)
print(nums)

heap_sort(nums)
print(nums)