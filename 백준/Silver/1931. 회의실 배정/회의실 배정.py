a = int(input())
meeting = []
result_meeting = []
count = 1
k = 0
for i in range(a):
    start, end = map(int, input().split())
    meeting.append([start,end])

meeting.sort(key = lambda x : (x[1],x[0]))
result_meeting.append(meeting[0])

for i in range(1,a):
    if meeting[i][0] >= result_meeting[k][1]:
        k += 1
        result_meeting.append(meeting[i])

print(len(result_meeting))