#include <vector>
#include <climits>
#include <iostream>
#include <algorithm>

using namespace std;

#define REP(i, n) for(int i = 0; i < (int)(n); ++ i)
#define FOR(i, b, e) for(auto i = b; i < e; ++ i)

typedef vector<int> VI;

int answer = 0;
int max_answer = INT_MIN;
int min_answer = INT_MAX;

void solve(int cur, const VI nums, VI& ops) {
    if(cur == nums.size()) {
        max_answer = max(answer, max_answer);
        min_answer = min(answer, min_answer);
    }

    int before = answer;

    // Order: + - x /
    FOR(i, 0, 4) {
        if(ops[i] != 0) {
            ops[i] -= 1;
            switch(i) {
                case 0:
                    answer += nums[cur];
                    break;
                case 1:
                    answer -= nums[cur];
                    break;
                case 2:
                    answer *= nums[cur];
                    break;
                case 3:
                    answer /= nums[cur];
                    break;
            }
            solve(cur+1, nums, ops);
            ops[i] += 1;
            answer = before;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int N, x;
    VI nums, ops;
    cin >> N;
    REP(i, N) {
        cin >> x;
        nums.push_back(x);
    }
    REP(i, 4) {
        cin >> x;
        ops.push_back(x);
    }

    answer = nums[0];
    solve(1, nums, ops);

    cout <<  max_answer << '\n';
    cout <<  min_answer << '\n';
    return 0;
}
