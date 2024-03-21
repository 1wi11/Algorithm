cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
b = a
c = []
for i in cro:
    count = a.count(i)
    c.append(count)
    a = a.replace(i,"*")

print(sum(c) + len(a) - a.count('*'))