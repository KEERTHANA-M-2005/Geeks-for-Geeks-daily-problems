# Given two strings s1 and s2. You have to check that s1 is a subsequence of s2 or not.
# Note: A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

# Examples:

# Input: s1 = "AXY", s2 = "YADXCP"
# Output: false
# Explanation: s1 is not a subsequence of s2 as 'Y' appears before 'A'.


def isSubSeq(s1, s2):
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    return i == len(s1)

s1 = "gksrek"
s2 = "geeksforgeeks" 
res = isSubSeq(s1, s2)
print(res)
    