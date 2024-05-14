import sys
from collections import deque

a = int(sys.stdin.readline())
q = deque()

for _ in range(a):
    b = sys.stdin.readline().split()

    if b[0] == 'push':
        q.append(int(b[1]))

    elif b[0] == 'pop':
        if q:
           print(q[0]) 
           q.popleft()
        else:
            print(-1)

    elif b[0] == 'size':
        print(len(q))

    elif b[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)

    elif b[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])

    elif b[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])