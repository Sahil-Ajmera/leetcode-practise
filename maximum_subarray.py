from math import inf
from typing import List
"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

"""
Optimized brute force
Time: O(N^2)
Space: O(1)
"""


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -inf

        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum > max:
                    max = sum

        return max


print(Solution1().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


"""
Kadane's Algorithm

Compute every sub array maximum and use it to calculate the maximu

Time: O(N)
Space: O(1)
"""


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = current_maximum = nums[0]

        for i in range(1, len(nums)):

            current_maximum = max(nums[i], current_maximum + nums[i])
            maximum = max(current_maximum, maximum)

        return maximum


print(Solution2().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


"""
Divide and Conquer

Time: O(N log N)
Space: O(log N)
"""


class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubArray(nums, left, right):

            if left > right:
                return -inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(curr, best_left_sum)

            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            best_combined_sum = nums[mid] + best_right_sum + best_left_sum

            left_half = findBestSubArray(nums, left, mid - 1)
            righ_half = findBestSubArray(nums, mid + 1, right)

            return max(left_half, righ_half, best_combined_sum)
        return findBestSubArray(nums, 0, len(nums) - 1)


print(Solution3().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
