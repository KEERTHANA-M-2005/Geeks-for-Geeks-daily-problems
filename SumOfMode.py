# Given an array arr[] of positive integers and an integer k. You have to find the sum of the modes of all the subarrays of size k.
# Note: The mode of a subarray is the element that occurs with the highest frequency. If multiple elements have the same highest frequency, the smallest such element is considered the mode.

# Examples:

# Input: arr[] = [1, 2, 3, 2, 5, 2, 4, 4], k = 3
# Output: 13
# Explanation: The mode of each k size subarray is [1, 2, 2, 2, 2, 4] and sum of all modes is 13.

from collections import Counter
def SumOfMode(arr, k):
    n = len(arr)
    if k > n:
        return 0
    freq = Counter(arr[:k])
    total_sum = 0
    def get_Mode(freq):
        max_count = max(freq.values())
        return min([num for num, count in freq.items() if count == max_count])
    total_sum += get_Mode(freq)
    
    for i in range(1, n-k+1):
        left = arr[i-1]
        freq[left] -= 1
        if freq[left] == 0:
            del freq[left]
        right = arr[i+k-1]
        freq[right] += 1
        total_sum += get_Mode(freq)
    return total_sum

arr = [2, 5, 1, 2, 6, 2, 6, 9, 3]
k = 2
res = SumOfMode(arr, k)
print(res)