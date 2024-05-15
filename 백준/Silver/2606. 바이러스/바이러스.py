def dfs(idx):
    global visited
    global answer
    visited[idx] = True
    answer.append(idx)
    for next in range(1,a+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)

a = int(input()) # 노드의 수 = 컴퓨터의 수
b = int(input()) # 간선의 수 = 연결된 쌍의 수

graph = [[False] * (a+1) for _ in range(a+1)]
visited = [False] * (a+1)
answer = []

for _ in range(b):
    c, d = map(int,input().split())
    graph[c][d] = True
    graph[d][c] = True

dfs(1)
print(len(answer)-1)