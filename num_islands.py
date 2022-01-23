"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

Time Complexity: O(M * N)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_islands: int = 0
            
            
        def back_tracking(grid, i, j):
            
            grid[i][j] = "0"
            
            for i_change, j_change in [(0,1), (1, 0), (-1, 0), (0, -1)]:
                
                if i + i_change >= 0 and i + i_change < len(grid) and j + j_change >= 0 and j + j_change < len(grid[0]) and grid[i + i_change][j + j_change] == "1":
                    back_tracking(grid, i + i_change, j + j_change)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == "1":
                    num_islands += 1
                    back_tracking(grid, i, j)
                    
        return num_islands
