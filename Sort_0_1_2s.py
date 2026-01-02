# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.

# Examples:

# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.


class Solution:
    def sort012(self, arr):
        if len(arr)>1:
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            
            self.sort012(left)
            self.sort012(right)

            i = j = k =0
            while i< len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
        return arr 