def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

a = int(input())
for _ in range(a):
    N, M = map(int,input().split())
    result = factorial(M) // (factorial(N) * factorial(M-N))
    print(result)