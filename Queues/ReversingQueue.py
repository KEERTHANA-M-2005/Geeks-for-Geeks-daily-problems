class Solution:
    def ReversingQueue(q):
        st = []
        while q:
            st.append(q[0])
            q.popleft()
            
        while st:
            q.append(st.pop())
            

q = [10, 20, 30, 40, 50]
print(q)
Solution.ReversingQueue(q)
while q:
    print(q.popleft(), end=" ")