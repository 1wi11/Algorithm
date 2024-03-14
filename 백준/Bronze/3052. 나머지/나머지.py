b = []

for _ in range (10):
    a = int(input())
    c = a%42
    
    if c not in b:
        b.append(c)

print(len(b))