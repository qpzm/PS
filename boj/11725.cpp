//https://www.geeksforgeeks.org/graph-implementation-using-stl-for-competitive-programming-set-1-dfs-of-unweighted-and-undirected/
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

void dfs_util(int u, const vector<int> adj[], vector<int> &visited) {
    for(auto v : adj[u])
        if(visited[v] == -1) {
            visited[v] = u;
            dfs_util(v, adj, visited);
        }
}

void add_edge(vector<int> adj[], int u, int v) {
    adj[u].push_back(v);
    adj[v].push_back(u);
}

int main() {
    int V = 100001;
    vector<int> adj[V];
    vector<int> visited(V, -1);
    int n, u, v;
    cin >> n;
    for(int i = 0; i < n; ++i) {
        cin >> u >> v;
        add_edge(adj, u, v);
    }

    for(int u=1; u<=n; ++u)
        if(visited[u] == -1) {
            visited[u] = u;
            dfs_util(u, adj, visited);
        }

    for(int i = 2; i <= n; ++i)
        cout << visited[i] << '\n';
    return 0;
}
