#include<iostream>
#include<string>
#include<vector>
using namespace std;

int N;
vector<string> V;

void Input(){
    cin >> N;
    for(int i = 0; i < N; i++){
        string S;
        cin >> S;
        V.push_back(S);
    }
}

int Is_Pal(int Left, int Right, int Delete, string Str){
    while(Left < Right){
        if(Str[Left] != Str[Right]){
            if(Delete == 0){
                if(Is_Pal(Left + 1, Right, 1, Str) == 0 || Is_Pal(Left,Right - 1, 1, Str) == 0){
                    return 1;
                }
                return 2;
            }
            else return 2;
        }
        else{
            Left++;
            Right--;
        }
    }
    return 0;
}

void Solution(){
    for(int i = 0; i < N; i++){
        string Str = V[i];
        int Result = Is_Pal(0, Str.length() - 1, 0, Str);
        cout << Result << endl;
    }
}

void Solve(){
    Input();
    Solution();
}

int main(void) {
    Solve();
}