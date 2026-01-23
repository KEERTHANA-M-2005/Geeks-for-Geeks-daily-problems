# Given an array arr[] containing only non-negative integers, your task is to find a continuous subarray (a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of the leftmost and rightmost elements of this subarray. You need to find the first subarray whose sum is equal to the target.

# Note: If no such array is possible then, return [-1].

# Examples:

# Input: arr[] = [1, 2, 3, 7, 5], target = 12
# Output: [2, 4]
# Explanation: The sum of elements from 2nd to 4th position is 12.

def subarray_Sum(arr, target):
    n = len(arr)
    cur_sum = 0
    left = 0
    
    for right in range(n):
        cur_sum += arr[right]
        
        while cur_sum > target and left <= right:
            cur_sum -= arr[left]
            left += 1

            if cur_sum == target:
                return [left+1, right+1]
    return [-1]