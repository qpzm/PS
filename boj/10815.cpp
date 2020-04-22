#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int N, M, n, target;
    vector<int> v;
    cin >> N;
    for(int i = 0; i < N; ++i) {
        cin >> n;
        v.push_back(n);
    }
    sort(v.begin(), v.end());
    cin >> M;

    for(int i = 0; i < M; ++i) {
        cin >> target;
        int d = M / 2;
        auto it = v.begin();

        while(d > 0) {
            while(next(it, d) < v.end() && *next(it, d) <= target) it = next(it, d);
            d /= 2;
        }
        if(*it == target)
            cout << 1 << '\n';
        else
            cout << 0 << '\n';
    }
    return 0;
}
