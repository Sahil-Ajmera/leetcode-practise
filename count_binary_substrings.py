"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 

Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

 

Constraints:

    1 <= s.length <= 105
    s[i] is either '0' or '1'.


"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:        
        prev = s[0]
        result = 0
        occurence_dict = {'0' : 0, '1': 0}
        
        for i in range(len(s)):
            if i == 0:
                occurence_dict[s[i]] = 1
                prev = s[i]
            elif prev == s[i]:
                occurence_dict[s[i]] += 1
                if s[i] == '0' and occurence_dict['1'] >= occurence_dict['0']:
                    result += 1
                if s[i] == '1' and occurence_dict['0'] >= occurence_dict['1']:
                    result += 1
            else:
                prev = s[i]
                result += 1
                occurence_dict[s[i]] = 1
        return result
        
