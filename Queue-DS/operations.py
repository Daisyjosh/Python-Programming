from collections import deque

q = deque()

q.append(10)
q.append(20)
q.append(30)

print(q[0]) # front ->10

q.popleft()

print(q[0])

