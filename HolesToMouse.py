# We are given two arrays mices[] and holes[] of same size. The mices[] represents the positions of the mice on a straight line, while holes[] represents the positions of the holes. Each hole can accommodate exactly one mouse. A mouse can either stay in its current position, move one step to the right, or move one step to the left, and each move takes one minute. We have to assign each mouse to a distinct hole in such a way that the time taken by the last mouse to reach its hole is minimized.

# Examples: 

# Input : mices[] = [4, -4, 2] , holes[] = [4, 0, 5]
# Output :  4
# Explanation: Assign the mouse at position 4 to the hole at position 4, so the time taken is 0 minutes. 
# Assign the mouse at position −4 to the hole at position 0, so the time taken is 4 minutes.
# Assign the mouse at position 2 to the hole at position 5, so the time taken is 3 minutes. Hence, the maximum time required by any mouse is 4 minutes 

def HolesToMouse(mices, holes):
    mices.sort()
    holes.sort()
    n = len(mices)
    max = 0
    for i in range(n):
        if (max < abs(mices[i] - holes[i])):
            max = abs(mices[i] -holes[i])
    return max

mices = [4, -4, 2]
holes = [4, 0, 5]
res = HolesToMouse(mices, holes)
print(res)