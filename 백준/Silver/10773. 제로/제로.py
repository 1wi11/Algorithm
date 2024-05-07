import sys
a = int(sys.stdin.readline())
stack = []

for _ in range(a):
    b = int(sys.stdin.readline())
    if b != 0:
        stack.append(b)
    else:
        stack.pop()

print(sum(stack))