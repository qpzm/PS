#include <vector>
#include <iostream>

using namespace std;

bool dfs(const vector<vector<int>>& adj, vector<int>& visited, int src) {
    int want_to_put = (visited[src] == 1) ? 2 : 1;
    bool res = true;

    for(auto u: adj[src]) {
        if(visited[u]) {
            res = res && (visited[u] == want_to_put);
        } else {
            visited[u] = want_to_put;
            res = res && dfs(adj, visited, u);
        }
    }

    return res;
}

bool solve(const vector<vector<int>>& adj) {
    bool res=true;
    vector<int> visited(adj.size()); // 0: unvisited, 1: set1, 2: set2
    for(int i=0; i<adj.size(); i++) {
        if(!visited[i]) {
            visited[i] = 1; // Always put the start vertex in set1
            res = res && dfs(adj, visited, i);
        }
    }

    return res;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int T, V, E, u, v;
    cin >> T;
    while(T--) {
        cin >> V >> E;
        vector<vector<int>> adj(V);
        for(int i=0; i<E; i++) {
            cin >> u >> v;
            adj[u-1].push_back(v-1);
            adj[v-1].push_back(u-1);
        }

        if(solve(adj)) {
            cout << "YES" << '\n';
        } else {
            cout << "NO" << '\n';
        }
    }

   //Testcase which I got wrong.
   //int V = 4;
   //vector<vector<int>> adj= {{1,2,3}, {0,2}, {0,1,3}, {0,2}};
   //solve(adj);
}
