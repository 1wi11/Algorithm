N, M = map(int, input().split())
my_basket = [i for i in range(1,N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    k = my_basket[a-1]
    my_basket[a-1] = my_basket[b-1]
    my_basket[b-1] = k
    
print(*my_basket)