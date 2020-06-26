#include <vector>
#include <iostream>
#include <algorithm>

#define MAX_LEN 1000
#define MAX_COST 1000
using namespace std;

vector<vector<int>> costs; // N * 3
vector<vector<int>> dp(3); // 3 * 3
int N;

void solve(int c) {
    vector<int>& prev_dp = dp[c];
    vector<int> cur_dp(3);
    int cur_cost, prev_min;

    for(int n=1; n<N; n++) {
        for(int i=0; i<3; i++) { // cur color
            cur_cost = costs[n][i];
            prev_min = INT_MAX;
            for(int j=0; j<3; j++) { // prev color
                if(i==j) continue;
                prev_min = min(prev_min, prev_dp[j]);
            }
            cur_dp[i] = cur_cost + prev_min;
        }
        prev_dp = cur_dp;
    }

    dp[c] = cur_dp;
}

// 2<= N <= 1000
int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int res, x;
    cin >> N;

    for(int i=0; i<N; i++) {
        vector<int> v;
        for(int j=0; j<3; j++) {
            cin >> x;
            v.push_back(x);
        }
        costs.push_back(v);
    }

    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if(i==j) {
                dp[i].push_back(costs[0][i]);
            }
            else {
                dp[i].push_back(3 * MAX_COST);
            }
        }
        solve(i);
    }

    res = dp[0][1];
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            if(i==j) continue;
            res = min(res, dp[i][j]);
        }
    }

    cout << res << '\n';
}
