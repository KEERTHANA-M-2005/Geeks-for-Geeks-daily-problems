# You are given two strings pat and tar consisting of lowercase English characters. You can construct a new string s by performing any one of the following operation for each character in pat:

# Append the character pat[i] to the string s.
# Delete the last character of s (if s is empty do nothing).
# After performing operations on every character of pat exactly once, your goal is to determine if it is possible to make the string s equal to string tar.

# Examples:

# Input: pat = "geuaek", tar = "geek"
# Output: true
# Explanation: Append the first three characters of pat to s, resulting in s = "geu". Delete the last character for 'a', leaving s = "ge". Then, append the last two characters 'e' and 'k' from pat to s, resulting in s = "geek", which matches tar.

class Solution:
    def StringStack(pat, tar):
        i = len(pat)-1
        j = len(tar)-1
        
        while i >= 0 and j >=0:
            if pat[i] == tar[j]:
                i -= 1
                j -= 1
            else:
                i -= 2
        return j < 0

pat = "geuaek"
tar = "geek"
res = Solution.StringStack(pat, tar)
print(res)