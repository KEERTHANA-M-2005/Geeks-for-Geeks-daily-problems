# Given the first 2 terms a1 and a2 of an Arithmetic Series. Find the nth term of the series. 

# Examples:

# Input: a1 = 2, a2 = 3, n = 4
# Output: 5
# Explanation: The series is: 2,3,4,5,6.... Thus, the 4th term is 5.



# Method1: Naive approach
def AP(a1, a2, n):
    ans = a1
    d = a2 - a1
    for i in range(1,n):
        ans += d
    return ans


# Method 2: Best approach
def AP(a1, a2, n):
    return a1+(n-1)*(a2-a1)