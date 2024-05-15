while True:
    a = input()
    stack = []
    if a[0] == '.':
        break
    b = len(a)
    for i in range(b):
        if a[i] == '(':
            stack.append(a[i])
        elif a[i] == '[':
            stack.append(a[i])
        elif a[i] == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
        elif a[i] == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if not stack:
            print('yes')
        else:
            print('no')
            