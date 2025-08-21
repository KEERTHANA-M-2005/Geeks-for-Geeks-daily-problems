# Given an array arr[] of integers and an integer k, select k elements from the array such that the minimum absolute difference between any two of the selected elements is maximized. Return this maximum possible minimum difference.

# Input: arr[] = [2, 6, 2, 5], k = 3
# Output: 1
# Explanation: 3 elements out of 4 elements are to be selected with a minimum difference as large as possible. Selecting 2, 2, 5 will result in minimum difference as 0. Selecting 2, 5, 6 will result in minimum difference as 6 - 5 = 1.


def MaxMinDif(arr, k):
    n = len(arr)
    if k <= 1 or n <= 1:
        return 0
    arr.sort()
    
    def can(d):
        count = 1
        last = arr[0]
        for x in arr[1:] :
            if x - last >= d :
                last = x
                count += 1
                
                if count >= k :
                    return True
        return False
    
    start, end, mid = 0, arr[-1]-arr[0], 0
    while start <= end :
        mid = (start + end) // 2
        if can(mid):
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans
    
arr = [1, 4, 9, 0, 2, 13, 3]
k = 4
sol = MaxMinDif(arr, k)
print("The  Maximum possible minimum defference is : " ,sol)