a = int(input())

for _ in range(a):
    b, c = input().split()
    b = int(b)
    for i in range(0,len(c)):
        print(c[i]*b,end = '')
    print()