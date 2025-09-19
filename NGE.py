# Given a circular integer array arr[], the task is to determine the next greater element (NGE) for each element in the array.

# The next greater element of an element arr[i] is the first element that is greater than arr[i] when traversing circularly. If no such element exists, return -1 for that position.

# Note: Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once.

# Examples: 

# Input: arr[] = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation:
# The next greater element for 1 is 3.
# The next greater element for 3 is 4.
# The next greater element for 2 is 4.
# The next greater element for 4 does not exist, so return -1.

def NextGeneratedElement(self, arr):
    n = len(arr)
    res = [-1]*n 
    st = []
    for i in range(2*n):
        while st and arr[i%n] >= arr[st[-1]]:
            idx = st.pop()
            res[idx] = arr[i % n]
        if i < n:
            st.append(i)
    return res

arr = [1, 4, 2 , 6, 3, 5, 2]
arr2 = NextGeneratedElement(0, arr)
print(arr2)