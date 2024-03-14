orig_chess = [1,1,2,2,2,8]
chess_receive = list(map(int, input().split()))
solution = []

for i in range(0,6):
    if orig_chess[i] != chess_receive[i]:
        if orig_chess[i] > chess_receive[i]:
            solution.append(orig_chess[i] - chess_receive[i])
        else:
            solution.append(orig_chess[i] - chess_receive[i])
    else:
        solution.append(0)

print(*solution)