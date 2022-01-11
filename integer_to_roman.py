"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman_string = ""
        
        predefined_positive_romans = [(1, "I"), (5, "V"), (10, "X"), (50, "L"), (100, "C"),
                                     (500, "D"), (1000, "M"), (900, "CM"), (400, "CD"), (40, "XL"), (90, "XC"), (4, "IV"), (9, "IX")]        
        while num > 0:
            closest_positive_num = predefined_positive_romans[0][0]
            closest_positive_roman = predefined_positive_romans[0][1] 
            for predefined_roman_tup in predefined_positive_romans:
                if num - predefined_roman_tup[0] >= 0 and abs(num - predefined_roman_tup[0]) < abs(num - closest_positive_num):
                    closest_positive_num = predefined_roman_tup[0]
                    closest_positive_roman = predefined_roman_tup[1]
                    
            num -= closest_positive_num
            roman_string += closest_positive_roman
            # predefined_positive_romans.sort(key=lambda k: abs(num-k[0]))
            # for predefined_num_tuple in predefined_positive_romans:
            #     if num - predefined_num_tuple[0] >= 0:
            #         num -= predefined_num_tuple[0]
            #         roman_string += predefined_num_tuple[1]
            #         break
        return roman_string
                
            
            
        
