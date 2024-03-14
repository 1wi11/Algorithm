N, M = map(int, input().split())
my_basket = [0] * N

for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a-1,b):
        my_basket[i] = c

print(*my_basket)
    
    