N, M = map(int, input().split())
my_basket = [i for i in range(1,N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    c = my_basket[a-1:b]
    c.reverse()
    my_basket[a-1:b] = c

print(*my_basket)