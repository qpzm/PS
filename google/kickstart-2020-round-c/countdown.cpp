#include <iostream>

using namespace std;

int main() {
    int T, N, K, x;
    int answer;
    cin >> T;

    for(int i=0; i<T; i++) {
        cin >> N >> K;
        int target = K;
        while(N--) {
            cin >> x;
            if(x == target) {
                target--;
                if(target == 0) {
                    answer += 1;
                    target = K;
                }
            } else if(x == K){
                target = K - 1;
            } else {
                target = K;
            }
        }
        cout << "Case #" << i+1 << ":"  << " " << answer << '\n';
        answer = 0;
    }
}
