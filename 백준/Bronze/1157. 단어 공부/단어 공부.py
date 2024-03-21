a = input().upper()
b = []
c = []

for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])

for i in b:
    count = a.count(i)
    c.append(count)


if c.count(max(c)) > 1:
    print('?')
else :
    max_index = c.index(max(c))
    print(b[max_index])