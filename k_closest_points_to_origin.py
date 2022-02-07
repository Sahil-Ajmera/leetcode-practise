import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        """
        # Solution using heaps
        # Time Complexity: O(N*log K)
        # return heapq.nsmallest(k, points, key = lambda point: math.sqrt(point[0]**2 + point[1]**2))
        
        # Solution using Binary search
        # Time Complexity: O(N)
#         distances = [point[0]**2 + point[1]**2 for point in points]
#         low = 0
#         high = max(distances)
#         result = []
#         remaining = [i for i in range(len(points))]
        
#         def split(remaining, distances, mid):
#             closer, farther = [], []
#             for index in remaining:
#                 if distances[index] <= mid:
#                     closer.append(index)
#                 else:
#                     farther.append(index)
#             return closer, farther
#         while k:
#             mid = (low + high) / 2
#             closer, farther = split(remaining, distances, mid)
#             if len(closer) > k:
#                 remaining = closer
#                 high = mid
#             else:
#                 k -= len(closer)
#                 result.extend(closer)
#                 remaining = farther
#                 low = mid
        
#         return [points[i] for i in result]

        
        # Solution using QuickSelect
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        def quick_select():
            
            left = 0
            right = len(points) - 1
            pivot_index = len(points)
            
            while pivot_index != k:
                
                pivot_index = partition(left, right)
                if pivot_index < k:
                    left = pivot_index
                else:
                    right = pivot_index - 1
                    
            return points[:k]
                    
        def partition(left, right):
            
            pivot = points[left + (right - left) // 2]
            pivot_dist = pivot[0]**2 + pivot[1]**2
            while left < right:
                if points[left][0]**2 + points[left][1]**2 >= pivot_dist:
                    points[left], points[right] = points[right], points[left]
                    right -= 1
                else:
                    left += 1
            if points[left][0]**2 + points[left][1]**2 < pivot_dist:
                left += 1
            return left
        
        return quick_select()
            
        
        
        
        
        
        
