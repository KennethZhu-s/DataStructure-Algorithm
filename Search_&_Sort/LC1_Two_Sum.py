"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
ex:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution1:    # O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [i,j]


class Solution2:     # O(nlogn)
    def binary_search(self, nums, left, right, val):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] == val:
                return mid
            elif nums[mid][0] > val:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_nums = [[num, i] for i, num in enumerate(numbers)]
        new_nums.sort(key=lambda x: x[0])

        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_search(new_nums, i + 1, len(new_nums) - 1, b)
            else:
                j = self.binary_search(new_nums, 0, i - 1, b)
            if j:
                break
        return [new_nums[i][1], new_nums[j][1]]