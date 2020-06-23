#include <iostream>

using namespace std;

int main() {
    int N;
    bool answer;
    cin >> N;
    if(4 <= N && N % 2 == 0) {
        cout << "YES" << '\n';
    } else {
        cout << "NO" << '\n';
    }
}
