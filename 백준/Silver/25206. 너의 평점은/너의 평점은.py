level1 = ['F','D0','D+','C0','C+','B0','B+','A0','A+']
level2 = [0.0,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]

degree = 0
total = 0
for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        degree += b
        total += b * level2[level1.index(c)]

print('%.6f' % (total/degree))