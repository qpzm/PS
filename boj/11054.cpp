#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define INPUT_MAX 1000

vector<int> lis(const vector<int> input) {
    vector<int> res;
    vector<int> min_here(input.size(), INPUT_MAX);
    int i;

    for(auto x : input) {
        // upper bound는 1 2 2 1 이렇게 같은 원소가 있으면 LIS 길이를 증가시켜서 안 됨.
        i = lower_bound(min_here.begin(), min_here.end(), x) - min_here.begin();
        min_here[i] = min(min_here[i], x);
        res.push_back(i + 1);
    }

    return res;
}

int bitonic(vector<int> input) {
    int res = 0, local;

    vector<int> v1 = lis(input);
    reverse(input.begin(), input.end());
    vector<int> v2 = lis(input);

    for(int i=0; i<v1.size(); ++i)  {
        // v2는 input의 역순의 LIS이므로 v2[i] = LIS([n-1, n-1-i])
        // v1[i] = LIS([0, i]) 이므로 이어붙이려면 v2[n-i-1] = LIS[n-1, i] = LDS[i, n-1] 이 필요.
        local = v1[i] + v2[v1.size() - 1 - i] - 1;
        res = max(res, local);
    }

    return res;
}

int main() {
    int N, x;
    cin >> N;
    vector<int> input;

    for(int i = 0; i < N; ++i) {
        cin >> x;
        input.push_back(x);
    }

    cout << bitonic(input) << '\n';
}
