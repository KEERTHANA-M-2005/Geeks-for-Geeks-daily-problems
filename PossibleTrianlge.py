# Given an integer array arr[]. 
# Find the number of triangles that can be formed with three different array elements as lengths of three sides of the triangle. A triangle with three given sides is only possible if sum of any two sides is always greater than the third side.

# Examples:

# Input: arr[] = [4, 6, 3, 7]
# Output: 3
# Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7]. Note that [3, 4, 7] is not a possible triangle. 

def NumofPossibleTriangle(arr):
    n = len(arr)
    arr.sort()
    count = 0
    for k in range(n-1, 1, -1):
        i, j = 0, k-1
        
        while i < j:
            if arr[i] + arr[j] > arr[k]:
                count += (j-i)
                j -= 1
            else:
                i += 1
    return count

arr = [10, 21, 22, 100, 101, 200, 300]
res = NumofPossibleTriangle(arr)
print(res)