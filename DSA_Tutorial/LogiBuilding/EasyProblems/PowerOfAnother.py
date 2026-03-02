# Given two positive integers x and y, determine if y is a power of x. If y is a power of x, return True. Otherwise, return False.

# Examples:

# Input: x = 2, y = 8
# Output: True 
# Explanation: 23 is equal to 8.

def isPower(x, y):
    if x == 1:
        return y == 1
    pow = 0
    while pow < y:
        pow *= x
    return pow == y
    