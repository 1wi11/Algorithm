#include<iostream>
#include<queue>
#include<vector>
using namespace std;

int N; //노드 수, 몇 명
int M; //간선 수, 비교한 횟수
int inDegree[32001] = {0, }; // 각 노드에 들어오는 간선의 수 0으로 초기화
vector<vector<int>> graph(32001);

void topology_sort() {
    queue<int> q;
    for (int i = 1; i <= N; i++){
        if (inDegree[i] == 0)
            q.push(i);
    }

    while (q.empty() == false){
        int now = q.front();
        cout << now << " ";
        q.pop();

        for(int k =0; k < graph[now].size(); k++){
            int next = graph[now][k];
            if(--inDegree[next] == 0)
                q.push(next);
        }
    }
}

int main() {
    int a, b;
    cin >> N >> M;
    for (int i = 0; i < M; i++){
        cin >> a >> b;
        //간선 추가
        graph[a].push_back(b); // 벡터의 끝에 요소를 추가한다
        inDegree[b]++;
    }

    topology_sort();
    return 0;
}
