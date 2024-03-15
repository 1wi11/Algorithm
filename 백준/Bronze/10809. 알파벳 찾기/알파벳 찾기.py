a = input()
b = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in range(0,len(alphabet)):
    if alphabet[i] in a :
        b.append(a.index(alphabet[i]))
    else:
        b.append(-1)

print(*b)