// Note! Sort the output
#include <iostream>
#include <algorithm>
#include <vector>
#define MAX 25
using namespace std;

char arr[MAX][MAX];

int bfs(char arr[][MAX], int n, int i, int j) {
    int res = 1;
    arr[i][j] = '2';
    if(0 <= i-1 && arr[i-1][j] == '1')
        res += bfs(arr, n, i-1, j);
    if(0 <= j-1 && arr[i][j-1] == '1')
        res += bfs(arr, n, i, j-1);
    if(i+1 < n && arr[i+1][j] == '1')
        res += bfs(arr, n, i+1, j);
    if(j+1 < n && arr[i][j+1] == '1')
        res += bfs(arr, n, i, j+1);
    return res;
}

int main() {
    int N, cnt;
    vector<int> v;
    char c;
    cin >> N;
    for(int i= 0; i < N; ++i) {
        for(int j= 0; j < N; ++j) {
            cin >> c;
            arr[i][j] = c;
        }
    }

    for(int i= 0; i < N; ++i) {
        for(int j= 0; j < N; ++j) {
            if(arr[i][j] == '1') {
                cnt = bfs(arr, N, i, j);
                v.push_back(cnt);
            }
        }
    }

    cout << v.size() << '\n';
    sort(v.begin(), v.end());
    for(auto x: v)
        cout << x << '\n';
    return 0;
}
