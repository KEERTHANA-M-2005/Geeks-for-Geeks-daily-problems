# Kadane’s Algorithm is a simple and powerful technique used to find the maximum sum of a contiguous subarray within a given array of integers (can include negative numbers).

# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[].

# Note : A subarray is a continuous part of an array.

# Examples:

# Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
# Output: 11
# Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
# Input: arr[] = [-2, -4]
# Output: -2
# Explanation: The subarray [-2] has the largest sum -2.


def kadnes_arr(arr):
    n = len(arr)
    cur_sum = arr[0]
    max_sum = arr[0]
    
    #Traversing through the array
    for i in range(1, n):
        cur_sum = max(arr[i], cur_sum+arr[i])
        
        max_sum = max(cur_sum, max_sum)
    return max_sum