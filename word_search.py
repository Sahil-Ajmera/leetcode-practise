"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Time Complexity: O(N * 3^L) N= number of cells on board L = length of word

Space Complexity: O(N) for visited matrix + O(L) call stack memory

If we update the input in place we have O(L) call stack memory
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def traversal_completes(current_matching_idx_word: int, current_x_matching_board: int, current_y_matching_board: int):
            if current_matching_idx_word == len(word):
                return True
            
            visited[current_x_matching_board][current_y_matching_board] = 1
            
            if current_x_matching_board + 1 < len(board) and visited[current_x_matching_board + 1][current_y_matching_board] == 0 and board[current_x_matching_board + 1][current_y_matching_board] == word[current_matching_idx_word] and traversal_completes(current_matching_idx_word + 1, current_x_matching_board + 1, current_y_matching_board):
                    return True
            if current_x_matching_board - 1 >= 0 and visited[current_x_matching_board - 1][current_y_matching_board] == 0 and board[current_x_matching_board - 1][current_y_matching_board] == word[current_matching_idx_word] and traversal_completes(current_matching_idx_word + 1, current_x_matching_board - 1, current_y_matching_board):
                    return True
            if current_y_matching_board + 1 < len(board[0]) and visited[current_x_matching_board][current_y_matching_board + 1] == 0 and board[current_x_matching_board][current_y_matching_board + 1] == word[current_matching_idx_word] and traversal_completes(current_matching_idx_word + 1, current_x_matching_board, current_y_matching_board + 1):
                    return True
            if current_y_matching_board - 1 >= 0 and visited[current_x_matching_board][current_y_matching_board - 1] == 0 and board[current_x_matching_board][current_y_matching_board - 1] == word[current_matching_idx_word] and traversal_completes(current_matching_idx_word + 1, current_x_matching_board, current_y_matching_board - 1):
                    return True
            
            visited[current_x_matching_board][current_y_matching_board] = 0
            return False

        
        
        for x_idx in range(len(board)):
            for y_idx in range(len(board[0])):
                
                if board[x_idx][y_idx] == word[0]:
                    if traversal_completes(1, x_idx, y_idx):
                        return True
                    
        return False
                    
                    
        
