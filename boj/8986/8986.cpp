#include <vector>
#include <iostream>

using namespace std;
typedef long long ll;

ll cost(vector<int> v, int n) {
    ll sum = 0;
    for(int i = 0; i < v.size(); ++i) {
        sum += abs(v[i] - n * i);
    }

    return sum;
}

ll binary_search(vector<int> v, int start, int end) {
    if(start == end) {
        return cost(v, start);
    }

    int m = (start + end) / 2;

    ll x = cost(v, m);
    ll y = cost(v, m + 1);

    if(x == y) {
        return x;
    }
    else if(x > y) {
        return binary_search(v, m + 1, end);
    } else {
        return binary_search(v, start, m);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
    int n, x, rightmost = -1;
    vector<int> v;
    cin >> n;

    for(int i = 0; i < n; ++i) {
        cin >> x;
        v.push_back(x);
    }

    for(int i = 1; i < n; ++i) {
        // rightmost가 정수가 아닌 경우 내림되어 꼭짓점의 상한이 아니게 된다.
        // 하지만 이 경우 x_1 / 1은 무조건 정수임이 보장되기 때문에 꼭짓점이
        // 최소 2개 이상이 된다. 따라서 가장 우측 꼭짓점이 최솟값일 수 없다.
        rightmost = max(rightmost, v[i] / i);
    }

    cout << binary_search(v, 1, rightmost) << '\n';
    return 0;
}
