"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Brute force
        
        Time Complexity: O(N^2)
        """
        answer = 0
        for idx in range(len(height)):
            
            left_max = 0
            for left_idx in range(0, idx):
                if height[left_idx] > left_max:
                    left_max = height[left_idx]
            
            right_max = 0
            for right_idx in range(len(height) - 1, idx, -1):
                if height[right_idx] > right_max:
                    right_max = height[right_idx]
                    
            saving = min(left_max, right_max) - height[idx]
            
            if saving > 0:    
                answer += saving
            
        return answer
    
        """
        left_max_arr = [0] * len(height)
        right_max_arr = [0] * len(height)
        
        left_max = 0
        for i in range(len(height)):
            if height[i] > left_max:
                left_max_arr[i] = height[i]
                left_max = height[i]
            else:
                left_max_arr[i] = left_max
        
        right_max = 0
        for i in range(len(height) - 1, -1, -1):
            if height[i] > right_max:
                right_max_arr[i] = height[i]
                right_max = height[i]
            else:
                right_max_arr[i] = right_max
        
        answer = 0
        for i in range(len(height)):
            saving = min(left_max_arr[i], right_max_arr[i]) - height[i]
            if saving > 0:
                answer += saving
                
        return answer
        
        """
