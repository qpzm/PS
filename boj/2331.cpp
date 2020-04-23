#include <iostream>
#include <unordered_map>
using namespace std;

int mul(int n, int m) {
    int res = 1;
    while(m--) {
        res *= n;
    }
    return res;
}

int next(int n, int m) {
    int res = 0;
    while(n % 10 != 0 || n / 10) {
        int right = n % 10;
        res += mul(right, m);
        n -= right;
        n /= 10;
    }

    return res;
}

int main() {
    int N, P;
    unordered_map<int, int> h;
    cin >> N >> P;
    int key = N;
    while(h.find(key) == h.end()) {
        h.insert({key, h.size()}); // Saves # of predecessors
        key = next(key, P);
    }
    cout << h[key] << '\n';
    return 0;
}
