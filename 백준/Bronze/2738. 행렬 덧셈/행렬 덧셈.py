a, b = [], []
N ,M = map(int, input().split())

for row in range(N):
    a.append(list(map(int, input().split())))

for row in range(N):
    b.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        result = a[i][j] + b[i][j]
        print(result, end= ' ')
    print()