#include<iostream>
#include<cstring>
#include<vector>
#include<queue>
using namespace std;

// 컴파일러에서 권장되는 초기화 방법 안하면 Warning이 뜰 수 있다
// 배열은 정적으로 선언되어야지 코드가 돌아감 -> 정적으로 쓰지 않을거면 동적 할당 사용해야함
void Input(int& M, int& N, vector<vector<int>>& T, queue<pair<int, int>>& q) {
    cin >> M >> N;
    // 1차원
    // vector <int>T(M*N);
    // 2차원
    T.resize(N, vector<int>(M));
    // RAII (Resouce Acquistion Is Intialization)
    // 벡터는 동적 메모리를 내부적으로 할당하고, 함수가 끝날 때 소멸자가 호출되어 자동으로 메모리 해제한다.
    for(int i = 0; i < N; i++){
        for(int j = 0 ; j < M; j++){
            cin >> T[i][j];
        }
    }

    for(int i = 0; i < N; i++){
        for(int j = 0 ; j < M; j++){
           if (T[i][j] == 1){
            q.push({i,j});
           }
        }
    }
}   

void Solution(int& M, int& N, vector<vector<int>>& T, queue<pair<int, int>>& q) {
    int dx[] = {-1, 1, 0, 0};  // 상, 하 이동
    int dy[] = {0, 0, -1, 1};  // 좌, 우 이동
    
    while (!q.empty()) {
        pair<int, int> pos = q.front();
        q.pop();

        int i = pos.first;
        int j = pos.second;

        for (int k = 0; k < 4; k++) {
            int nx = i + dx[k];  
            int ny = j + dy[k];  
  
            if (nx >= 0 && nx < N && ny >= 0 && ny < M && T[nx][ny] == 0) {
                T[nx][ny] = T[i][j] + 1;  
                q.push({nx, ny});  
            }
        }
    }

    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < M; j++) {
    //         cout << T[i][j] << " ";
    //     }
    //     cout << endl;
    // }

    // 결과 출력

    int max = T[0][0];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (T[i][j] == 0){
                cout << -1 << endl;
                return;
            }
            if (T[i][j] > max){
                max = T[i][j];
            }
        }
    }

    cout << max-1 << endl;
}

void Solve(){
    int M{0}, N{0};
    vector<vector<int>> T;        
    queue<pair<int, int>> q;
    Input(M, N, T, q);           
    Solution(M, N, T, q);  
}

int main(void) {
    Solve();
}