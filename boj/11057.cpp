#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, sum=0;
    vector<int> mem(10, 1);
    cin >> n;
    for(int i = 1; i < n; ++i) {
        for(int j = 0; j < 10; ++j) {
            mem[j] = (mem[j-1] + mem[j]) % 10007;
        }
    }

    for (auto& i : mem)
        sum = (sum + i) % 10007;

    cout << sum << '\n';
    return 0;
}
