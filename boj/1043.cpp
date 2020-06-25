// O(N^2 * M) solution: 최대 N명이 vector에 들어올 수 있고 1명 처리할 때마다 O(NM) 전체 matrix scan
// 1. 입력에 따라 진실을 아는 사람 벡터(truth)를 초기화.
// 2. 진실을 아는 사람들이 있는 파티를 찾는다.
// 3. 해당 파티에 참가한 사람들 중 벡터에 들어온 적 없었던 사람들만 다시 진실 벡터에 넣는다.
// 이 풀이는 파티 -> 사람, 사람 -> 파티를 찾는데 선형 시간이 든다.
// 양방향 모두 O(1)에 찾을 수 있도록 두 개의 자료구조를 만들면 그래프 방문 문제이므로 O(NM).
//
// TroubleShootings
// 1. 파티 참가자가 0인 케이스는 거짓말해도 되는지 아닌지 애매함.
//    여기서는 거짓말할 수 있는 것으로 처리. 테스트케이스에 해당 경우 없음.
// 2. bool array는 초기화하지 않으면 랜덤한 값이 들어 있었다.

#include <vector>
#include <iostream>

using namespace std;

int M, N, T, x;
bool parties[50][50] = {false};
vector<int> truth;

int solve(vector<int>& truth) {
    bool answer[50] = {false}; // row-wise
    bool visited[50] = {false}; // col-wise
    int res = M;

    while(truth.size() != 0) {
        int j = truth.back();
        truth.pop_back();
        visited[j] = true;

        for(int i=0; i<M; i++) {
            if(parties[i][j] && !answer[i]) {
                answer[i] = true;
                res--;

                for(int k=0; k<N; k++) {
                    if(parties[i][k] && !visited[k]) {
                        truth.push_back(k);
                    }
                }
            }
        }
    }

    return res;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cin >> N >> M >> T;

    while(T--) {
        cin >> x;
        truth.push_back(x-1);
    }

    for(int i=0; i<M; i++) {
        int total;
        cin >> total;

        while(total--) {
            cin >> x;
            parties[i][x-1] = true;
        }
    }

    cout << solve(truth) << '\n';
}
