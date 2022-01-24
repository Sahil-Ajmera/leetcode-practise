"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

 

Constraints:

    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        trie = {}
        
        result = []
        
        # Time Complexity: O(N) N is the total number of letters in the words in the input
        # Space Complexity: O(N)
        for word in words:
            curr = trie
            for letter in word:
                if letter in curr:
                    curr = curr[letter]
                else:
                    curr[letter] = {}
                    curr = curr[letter]
            curr['$'] = word
                    
        def dfs (i, j, trie):
            # Time Complexity: O(M * 3 ^ (L -1))
            
            match_node = trie[board[i][j]]
            
            if '$' in match_node:
                result.append(match_node.pop('$'))
            
            letter = board[i][j]
            board[i][j] = '#'
            for i_change, j_change in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if i + i_change >= 0 and i + i_change < len(board) and j + j_change >=0  and j + j_change < len(board[0]) and board[i + i_change][j + j_change] in match_node:
                    dfs(i + i_change, j + j_change, match_node)
                    
            board[i][j] = letter
            
            # Optimization: incrementally remove the leaf node that matched
            if not match_node:
                trie.pop(letter)
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    dfs(i, j, trie)
                    
        return result
                    
        
        
        
