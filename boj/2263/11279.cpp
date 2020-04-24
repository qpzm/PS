#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    int N;
    vector<int> v;
    cin >> N;
    while(N--) {
        int m;
        cin >> m;
        if(m != 0) {
            v.push_back(m);
            push_heap(v.begin(), v.end());
        } else if (v.size() != 0) {
            int max;
            pop_heap(v.begin(), v.end());
            max = v.back();
            v.pop_back();
            cout << max << '\n';
        } else {
            cout << 0 << '\n';
        }
    }
    return 0;
}
