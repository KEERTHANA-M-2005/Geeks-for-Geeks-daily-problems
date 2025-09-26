# You are given a deque dq (double-ended queue) containing non-negative integers, along with two positive integer type and k. The task is to rotate the deque circularly by k positions.
# There are two types of rotation operations:



# Right Rotation (Clockwise): If type = 1, rotate the deque to the right. This means moving the last element to the front, and repeating the process k times.
# Left Rotation (Anti-Clockwise): If type = 2, rotate the deque to the left. This means moving the first element to the back, and repeating the process k times.
# Examples:

# Input: dq = [1, 2, 3, 4, 5, 6], type = 1, k = 2
# Output: [5, 6, 1, 2, 3, 4] 
# Explanation: The type is 1 and k is 2. So, we need to right rotate dequeue by 2 times.
# In first right rotation we get [6, 1, 2, 3, 4, 5].
# In second right rotation we get [5, 6, 1, 2, 3, 4].


from collections import deque
def rotatedequeue(dq, type, k):
    if not isinstance(dq, deque):
        dq = deque(dq)
    n = len(dq)
    k = k % n
    
    if type == 1:
        for _ in range(k):
            dq.appendleft(dq.pop())
    else:
        for _ in range(k):
            dq.append(dq.popleft())
    return list(dq)

dq = [10, 20, 30, 40, 50]
type = int(input("Enter 1 or 2 : "))
k = int(input("Enter the Key: "))
res = rotatedequeue(dq, type, k)
print(res)