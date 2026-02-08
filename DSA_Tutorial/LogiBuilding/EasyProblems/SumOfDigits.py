# Given a number n, find the sum of its digits.

# Examples : 

# Input: n = 687
# Output: 21
# Explanation: The sum of its digits are: 6 + 8 + 7 = 21

# Input: n = 12
# Output: 3
# Explanation: The sum of its digits are: 1 + 2 = 3

def sumOfDigits(n):
    sum = 0
    if n == 0:
        return 
    
    while n != 0:
        l = n % 10
        sum += l
        n //= 10
    return sum 