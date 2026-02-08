# Given two integers n and m (m != 0). The problem is to find the number closest to n and divisible by m. If there is more than one such number, then output the one having the maximum absolute value.

# Examples :

# Input: n = 13, m = 4
# Output: 12
# Explanation: 12 is the Closest Number to 13 which is divisible by 4.


def closestNumber(n, m):
    q = int(n/m)
    n1 = m*q
    
    if n*m > 0:
        n2 = (m*(q+1))
    else:
        n2 = (m*(q-1))
    
    return n2 if abs(n-n1) > abs(n-n2) else n1
