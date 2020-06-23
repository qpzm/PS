#include <vector>
#include <iostream>

using namespace std;

void dfs(const vector<int>& v, vector<bool>& visited, int src) {
    visited[src] = true;
    int dest = v[src];
    if(visited[dest]) return;
    dfs(v, visited, dest);
}

int solve(const vector<int>& v) {
    int res=0;
    vector<bool> visited(v.size());
    for(int i=0; i<v.size(); i++) {
        if(!visited[i]) {
            res++;
            dfs(v, visited, i);
        }
    }

    return res;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int N, M, x, cycles;
    cin >> N;
    while(N--) {
        vector<int> v;
        cin >> M;
        for(int i=0; i<M; i++) {
            cin >> x;
            v.push_back(x - 1); // x starts from 1
        }

        cycles = solve(v);
        cout << cycles << '\n';
    }
}
