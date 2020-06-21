#include <bits/stdc++.h>

using namespace std;

int cnt[2] = {0, 0};
int arr[128][128];

void f(int i, int j, int n) {
    if(n == 0) return;
    int color = arr[i][j];

    bool same = true;
    for(int row=i; row < i + n; row++) {
        for(int col=j; col < j + n; col++) {
            if(arr[row][col] != color) {
                same = false;
                break;
            }
        }
    }
    vector<int> inputs = {i, j, n, same};

    if(same) {
        cnt[color] += 1;
        return;
    }

    f(i, j, n/2);
    f(i, j + n/2, n/2);
    f(i + n/2, j, n/2);
    f(i + n/2, j + n/2, n/2);
}

int main() {
    cin.sync_with_stdio(false);
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cin >> arr[i][j];
        }
    }

    f(0, 0, N);
    cout << cnt[0] << '\n';
    cout << cnt[1] << '\n';
}
