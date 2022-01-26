"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

 

Constraints:

    1 <= intervals.length <= 104
    0 <= starti < endi <= 106
"""

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            
            free_rooms = []
            
            intervals.sort(key = lambda k: k[0])
            
            heapq.heappush(free_rooms, intervals[0][1])
            
            for interval in intervals[1:]:
                
                if free_rooms[0] <= interval[0]:
                    heapq.heappop(free_rooms)
                
                heapq.heappush(free_rooms, interval[1])
                
            return len(free_rooms)
                
        
