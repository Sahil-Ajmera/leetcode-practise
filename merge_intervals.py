"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval_index in range(1, len(intervals)):
            last_merged_interval = result[-1]
            if intervals[interval_index][0] <= last_merged_interval[1]:
                result.pop()
                new_interval = [min(intervals[interval_index][0], last_merged_interval[0]), max(intervals[interval_index][1], last_merged_interval[1])]
                result.append(new_interval)
            else:
                result.append(intervals[interval_index])
        return result
