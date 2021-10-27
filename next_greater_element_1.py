from typing import List

"""
Brute force

Time complexity: O(M*N)
Space complexity: O(1)
"""


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums1)):
            found_match = False
            for j in range(0, len(nums2)):
                if nums1[i] == nums2[j]:
                    found_match = True
                    found_greater = False
                    for k in range(j, len(nums2)):
                        if nums2[k] > nums2[j]:
                            found_greater = True
                            res.append(nums2[k])
                            break
                    if not found_greater:
                        res.append(-1)
            if not found_match:
                res.append(-1)
        return res


print(Solution1().nextGreaterElement([2, 4], [1, 2, 3, 4]))


"""
Better brute force

Time complexity: O(M*N)
Space complexity: O(N)
"""


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        nums2_map = dict()
        for i in range(0, len(nums2)):
            nums2_map[nums2[i]] = i

        for i in range(0, len(nums1)):
            for j in range(nums2_map[nums1[i]], len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break

        return res


print(Solution2().nextGreaterElement([2, 4], [1, 2, 3, 4]))


"""
Using stacks

Time complexity: O(N)
Space Complexity: O(N)
"""


class Solution3:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        element_to_greater_than_element_map = dict()

        for i in range(0, len(nums2)):
            if len(stack) == 0:
                stack.append(nums2[i])
            else:
                found_greater = False
                while len(stack) != 0 and nums2[i] > stack[-1]:
                    found_greater = True
                    element_to_greater_than_element_map[stack[-1]] = nums2[i]
                    stack.pop()
                if found_greater:
                    stack.append(nums2[i])
                else:
                    element_to_greater_than_element_map[nums2[i]] = -1

        for i in range(len(stack)):
            element_to_greater_than_element_map[stack[i]] = -1
        res = []
        for i in range(len(nums1)):
            res.append(element_to_greater_than_element_map[nums1[i]])

        return res


print(Solution3().nextGreaterElement([2, 4], [1, 2, 3, 4]))
