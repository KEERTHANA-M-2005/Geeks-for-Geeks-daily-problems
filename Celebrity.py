# A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

# Note: Follow 0-based indexing.

# Examples:

# Input: mat[][] = [[1, 1, 0],
#                 [0, 1, 0],
#                 [0, 1, 1]]
# Output: 1
# Explanation: 0th and 2nd person both know 1st person and 1st person does not know anyone. Therefore, 1 is the celebrity person.

def celebrity(mat):
    n = len(mat)
    st = []
    
    for i in range(n):
        st.append(i)
        
    while len(st) > 1:
        a = st.pop()
        b = st.pop()
        if mat[a][b]:
            st.append(b)
        else:
            st.append(a)
    c = st.pop()
    for i in range(n):
        if i == c:
            continue
        if mat[c][i] or not mat[i][c]:
            return -1 
    return c

mat = [[1, 1, 0],[0, 1, 0],[0, 1, 1]]
print(celebrity(mat))