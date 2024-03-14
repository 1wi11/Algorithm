a = int(input())
score = list(map(int, input().split()))
max_score = max(score)
sum = 0
for i in range(0,a):
    sum += score[i]/max_score * 100

print(sum/a)