"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        O(NKlog(k))
        """
        
        sorted_string_map: Dict[tuple, list] = defaultdict(list)
        
        for s in strs:
            sorted_string_map[tuple(sorted(s))].append(s)
        
        return sorted_string_map.values()
    
        """
        
        Time Complexity : O(NK)
        strings_character_count_map: Dict[tuple, list]
        
        for s in strs:
            character_count_list = [0]*26
            for c in s:
                character_count_list[ord(c) - ord('a')] += 1
            strings_character_count_map[tuple(character_count_list)].append(s)
        return strings_character_count_map.values()
                
        
        """
        
