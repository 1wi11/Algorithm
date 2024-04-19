a = int(input())
for _ in range(a):
    e, c = map(int,input().split())
    b = e % 10
    
    if b == 1 or b == 5 or b == 6:
        print(b)
    elif b == 0:
        print('10')
    elif b == 4 or b == 9:
        d = c % 2
        if b == 4:
            if d == 0:
                print('6')
            else:
                print('4')
        elif b == 9:
            if d == 0:
                print('1')
            else:
                print('9')
    else:
        if b == 2:
            d = c % 4
            if d == 0:
                print('6')
            elif d == 1:
                print('2')
            elif d == 2:
                print('4')
            elif d == 3:
                print('8')
        elif b == 3:
            d = c % 4
            if d == 0:
                print('1')
            elif d == 1:
                print('3')
            elif d == 2:
                print('9')
            elif d == 3:
                print('7')
        elif b == 7:
            d = c % 4
            if d == 0:
                print('1')
            elif d == 1:
                print('7')
            elif d == 2:
                print('9')
            elif d == 3:
                print('3')
        elif b == 8 :
            d = c % 4
            if d == 0:
                print('6')
            elif d == 1:
                print('8')
            elif d == 2:
                print('4')
            elif d == 3:
                print('2')