def sift(nums, low, high):
    """
    :param nums: list
    :param low: heap's root position
    :param high: heap's last position
    :return:
    """
    i = low
    j = 2 * i + 1
    tmp = nums[low]
    while j <= high:
        if j+1 <= high and nums[j+1] < nums[j]:   # changed to min heap, before is max heap
            j = j + 1
        if nums[j] < tmp:
            nums[i] = nums[j]
            i = j
            j = 2 * i + 1
        else:
            nums[i] = tmp
            break
    else:
        nums[i] = tmp

def topk(nums, k):    # O(nlogk)
    heap = nums[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)      # build heap

    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heap[0] = nums[i]
            sift(heap, 0, k-1)  # traversial

    for i in range(k - 1, -1, -1):  # i always points the last element of heap
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)

    return heap

nums = [i for i in range(1,10)]
import random
random.shuffle(nums)
print(nums)
print(topk(nums, 3))

