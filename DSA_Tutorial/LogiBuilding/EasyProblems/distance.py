# Given coordinates of 2 points on a cartesian plane, find the distance between them round the result to the nearest integer.

# Example 1:

# Input: 0 0 2 -2
# Output: 3
# Explanation: Distance between (0, 0) 
# and (2, -2) is 3.
import math
def distance(x1, x2, y1, y2):
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2))