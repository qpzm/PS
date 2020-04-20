#include <vector>
#include <iostream>
using namespace std;

int main() {
    vector<int> stk;
    int V, E, u, v, res=0;
    cin >> V >> E;
    vector<int> adj[V+1];
    vector<bool> visited(V+1, false);
    while(cin >> u >> v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for(int i=1; i <= V; i ++) {
        if(!visited[i]) {
            res += 1;
            stk.push_back(i);
        }
        while(stk.size() != 0) {
            v = stk.back();
            stk.pop_back();
            if(!visited[v]) {
                visited[v] = true;
                for(auto neighbor : adj[v]) {
                    if(!visited[neighbor]) {
                        stk.push_back(neighbor);
                    }
                }
            }
        }
    }
    cout << res << '\n';
    return 0;
}
