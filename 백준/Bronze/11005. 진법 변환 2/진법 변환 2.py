a, b = map(int,input().split())
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = ''

while a:
    c += str(num_list[a%b])
    a //= b

print(c[::-1]) 