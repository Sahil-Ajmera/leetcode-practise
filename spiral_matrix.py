"""
Given an m x n matrix, return all elements of the matrix in spiral order.
"""

"""
Time complexity: O(M*N)
Space Complexity: O(1)
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left = 0
        right = len(matrix[0])
        top = 0
        down = len(matrix)
        direction =  0  # 0 for right, 1 for down, 2 for left, 3 for right
        
        while left < right and top < down:
            
            if direction == 0: # left to right
                
                for col in range(left, right):
                    result.append(matrix[top][col])
                    
                top += 1
            
            elif direction == 1: # top to bottom
                
                for row in range(top, down):
                    result.append(matrix[row][right - 1])
                    
                right -= 1
                
            elif direction == 2: # right to left
                
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down - 1][col])
                    
                down -= 1
                
            else:
                # bottom to top
                for row in range(down - 1, top - 1, -1):
                    result.append(matrix[row][left])
                    
                left += 1
                
            direction = (direction + 1) % 4
            
        return result
                    
        
