#include <iostream>
#include <algorithm>

using namespace std;
int main(){
    int N, a, best, sum;
    cin >> N >> sum;
    best = sum;
    for(int i=1; i<N; i++){
        cin >> a;
        sum = max(sum + a, a);
        best = max(sum, best);
    }
    cout << best << '\n';
}
