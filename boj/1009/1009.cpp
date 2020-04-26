#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> find_cycle(int n) {
    vector<int> v;
    int i = n;
    while(find(v.begin(), v.end(), i) == v.end()) {
        v.push_back(i);
        i = (i * n) % 10;
    }
    return v;
}

int main() {
    int N;
    vector<vector<int>> memo(10);
    /* Since a computer number is within [1 ~ 10]
     * Every number ends with 0 returns 10, not 0.
     */
    memo[0] = {10};

    cin >> N;
    while(N--) {
        int a, b;
        cin >> a >> b;
        a = a % 10;
        if(memo[a].size() == 0)
            memo[a] = find_cycle(a);

        int len = memo[a].size();
        if(len == 1)
            cout << memo[a][0] << '\n';
        else {
            // modulo 1 2 3 0
            // index  0 1 2 3
            cout << memo[a][(b + len - 1) % len] << '\n';
        }
    }
    return 0;
}
