#include <iostream>
using namespace std;

int main() {
    int N, M, K, teams, deficit;
    cin >> N >> M >> K;
    teams = min(N / 2, M);
    deficit = K - (N - teams * 2 + M - teams);
    if(0 < deficit) {
        teams -= deficit / 3;
        if(deficit % 3)
            teams -= 1;
    }
    cout << teams;
    return 0;
}
