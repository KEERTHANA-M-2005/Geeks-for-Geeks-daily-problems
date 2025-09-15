# Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
# An expression is balanced if:

# Each opening bracket has a corresponding closing bracket of the same type.
# Opening brackets must be closed in the correct order.
# Examples :

# Input: s = "[{()}]"
# Output: true
# Explanation: All the brackets are well-formed.
# Input: s = "[()()]{}"
# Output: true
# Explanation: All the brackets are well-formed.

from collections import deque
class Solution:
    def ParanthesisCheck(s):
        st = deque()
        for c in s:
            if (c == '(' or c == '{' or c == '['):
                st.append(c)
            elif (c == ')' or c == '}' or c == ']'):
                if not st:
                    return False
                top = st[-1]
                if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                    return False 
                st.pop()
        return not st
    
s ="{[()]}"
res = Solution.ParanthesisCheck(s)
print(res)