import sys
input = sys.stdin.readline
a, b = map(int,input().split())
num_type = []
answer = 0
for _ in range(a):
    c = int(input())
    num_type.append(c)

for i in range(len(num_type)-1,-1,-1):
    d = 0
    if num_type[i] > b:
        continue

    else:
        d = b // num_type[i]
        answer += d
        b = b - (d * num_type[i])
        if b == 0:
            break

print(answer)