class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Credits to https://www.youtube.com/watch?v=LPFhl65R7ww
        
        Explained well in video
        
        Time Complexity: O(log(min(m,n)))
        """
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        low = 0
        high = len(nums1)
        
        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (len(nums1) + len(nums2) + 1) // 2 - partitionX
            # Partitions are now created, we have a max_x_left_half, max_y_left_half
            # and min_x_right_half and min_y_right_half
            max_x_left_half = nums1[partitionX - 1] if partitionX != 0 else -inf
            max_y_left_half = nums2[partitionY - 1] if partitionY != 0 else -inf
            min_x_right_half = nums1[partitionX] if partitionX != len(nums1) else inf
            min_y_right_half = nums2[partitionY] if partitionY != len(nums2) else inf

            if max_x_left_half <= min_y_right_half and max_y_left_half <= min_x_right_half:
                # We have found the elements that are useful for consideration
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(max_x_left_half, max_y_left_half) + min(min_x_right_half, min_y_right_half)) / 2
                else:
                    return max(max_x_left_half, max_y_left_half)
            elif max_x_left_half > min_y_right_half:
                # PartitionX needs to move left
                high = partitionX - 1
            else:
                # PartitionX needs to move right
                low = partitionX + 1
