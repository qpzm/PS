#include <iostream>
using namespace std;

int main() {
    int N, res=1;
    cin >> N;
    while(N != 0)
        res *= N--;
    cout << res << '\n';
    return 0;
}
