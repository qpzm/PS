#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
int max_score(vector<int> scores[], int M) {
    int mem[3] = {0};
    int tmp[3];
    REP(i, M) {
        tmp[0] = max(mem[2], mem[1]) + scores[0][i];
        tmp[1] = max(mem[2], mem[0]) + scores[1][i];
        tmp[2] = max(mem[0], mem[1]);
        REP(j, 3)
            mem[j] = tmp[j];
    }
    return max(mem[0], max(mem[1], mem[2]));
}

int main() {
    int N, M, num;
    cin >> N;
    REP(i, N) {
        cin >> M;
        vector<int> scores[2];
        REP(j, 2) {
            REP(k, M) {
                cin >> num;
                scores[j].push_back(num);
            }
        }
        cout << max_score(scores, M) << '\n';
    }

    return 0;
}
