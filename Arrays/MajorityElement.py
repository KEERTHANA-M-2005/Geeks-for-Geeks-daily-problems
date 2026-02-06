# Given an array arr[]. Find the majority element in the array. If no majority element exists, return -1.

# Note: A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

# Examples:

# Input: arr[] = [1, 1, 2, 1, 3, 5, 1]
# Output: 1
# Explanation: Since, 1 is present more than 7/2 times, so it is the majority element.

class Solution:
    def majorityElement(self, arr):
        
        candidate = None
        count = 0
        
        # Step 1: Find candidate
        for num in arr:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        # Step 2: Verify candidate
        if arr.count(candidate) > len(arr)//2:
            return candidate
        
        return -1
