a = input()
c = int(len(a))
b = int(len(a)) // 2
count = 0
if c%2 == 1:
    for i in range(0,b):
        if a[i] == a[-(i+1)]:
            count += 1
else:
    for i in range(0,b):
        if a[i] == a[-(i+1)]:
            count += 1

if count == b:
    print("1")
else:
    print("0")