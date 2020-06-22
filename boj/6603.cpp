#include <vector>
#include <iostream>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)

typedef vector<int> VI;

VI answer;
bool visited[12];

void print(VI v) {
    for(auto x: v) {
        cout << x << ' ';
    }
    cout << '\n';
}

void solve(VI v, int begin) {
    if(answer.size() == 6) {
        print(answer);
        return;
    }

    FOR(i, begin, v.size()) {
        answer.push_back(v[i]);
        // If the last character of the answer is v[i], then start from v[i+1]
        solve(v, i + 1);
        answer.pop_back();
    }
}

int main() {
    cin.sync_with_stdio(false);ios::sync_with_stdio(false);cin.tie(NULL);
    int N, x;
    VI v;

    while(1) {
        v = {};
        cin >> N;
        if(N == 0) {
            break;
        }

        REP(i, N) {
            cin >> x;
            v.push_back(x);
        }
        solve(v, 0);
        cout << '\n';
    }

    return 0;
}
