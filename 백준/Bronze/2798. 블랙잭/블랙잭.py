num, max_num = map(int, input().split())
num_list = list(map(int, input().split()))
result = 0
for i in range(num):
    for j in range(i+1,num):
        for k in range(j+1,num):
            if num_list[i] + num_list[j] + num_list[k] > max_num:
                continue
            else:
                result = max(result, num_list[i] + num_list[j] + num_list[k])

print(result)