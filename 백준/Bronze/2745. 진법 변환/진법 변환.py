a, b = input().split()
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = a[::-1]
result = 0

for i,n in enumerate(a):
    result += (int(b)**i) * (num_list.index(n))

print(result)