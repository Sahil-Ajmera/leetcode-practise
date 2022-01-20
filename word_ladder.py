"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        one way of identifying no sequence exists is that the endWord is not part of the 
        word list
        
        Time Complexity: O(M^2 * N)
        """
        if endWord not in wordList:
            return 0
        
        word_transformation_dict = defaultdict(set)
        
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                word_transformation_dict[wordList[i][:j] + "*" + wordList[i][j+1:]].add(wordList[i])
                
        queue = collections.deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        
        while len(queue) != 0:
            
            word, level = queue.popleft()
            
            if word == endWord:
                return level
            
            for i in range(len(word)):
                
                transformer = word[:i] + "*" + word[i+1:]
                
                for new_transformation in word_transformation_dict[transformer]:
                    if new_transformation not in visited:
                        visited.add(new_transformation)
                        queue.append((new_transformation, level + 1))
        return 0
        
        
                        
            
        
