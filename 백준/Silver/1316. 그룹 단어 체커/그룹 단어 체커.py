a = int(input())
c = a 
for i in range(a):
    b = input()
    error = 0
    for j in range(len(b) - 1):
        if b[j] == b[j+1]:
            pass
        elif b[j] in b[j+1:]:
            c -= 1
            break

print(c)