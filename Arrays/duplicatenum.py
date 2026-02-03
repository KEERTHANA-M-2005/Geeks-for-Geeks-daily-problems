# Given an array arr[] of size n, containing elements from the range 1 to n, and each element appears at most twice, return an array of all the integers that appears twice.

# Note: You can return the elements in any order but the driver code will print them in sorted order.

# Examples:

# Input: arr[] = [2, 3, 1, 2, 3]
# Output: [2, 3] 
# Explanation: 2 and 3 occur more than once in the given array.

class Solution:
    def findDuplicates(self, arr):
        # code here552
        arr.sort()
        ans = []
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                if not ans or ans[-1] != arr[i]:
                    ans.append(arr[i])
        return ans