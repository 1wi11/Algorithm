import sys
def dfs(idx):
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1,N + 1):
        #next라는 노드가 방문한 적이 없고 방문할 수 있다면 방문 
        if not visited[next] and graph[idx][next]:
            dfs(next)

def bfs(): 
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end = ' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)
                
#0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int,input().split())
# 총 노드의 개수는 1~4번까지 총 4개가 있고
# 간선의 개수는 5개
# 시작 번호는 1
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N + 1)

#1. graph 정보 입력
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = True
    graph[b][a] = True

#2. dfs
dfs(V)
print()

#3. bfs
visited = [False] * (N + 1)
q = [V]
visited[V] = True
bfs()