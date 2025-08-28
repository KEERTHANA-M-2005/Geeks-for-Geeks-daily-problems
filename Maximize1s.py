# Given a binary array arr[] containing only 0s and 1s and an integer k, you are allowed to flip at most k 0s to 1s. 
# Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.

# Examples:

# Input: arr[] = [1, 0, 1], k = 1
# Output: 3
# Explanation: By flipping the zero at index 1, we get the longest subarray from index 0 to 2 containing all 1’s.


def maxOne(arr, k):
    count, res, start, end = 0, 0, 0, 0
    
    while end < len(arr):
        if arr[end] == 0:
            count += 1
        
        while count > k:
            if arr[start] == 0:
                count -= 1
            start += 1
        res = max(res, (end-start+1))
        end += 1
    return res

arr = [1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0]
k = 2
print(maxOne(arr, k))
            