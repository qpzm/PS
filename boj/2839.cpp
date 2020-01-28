#include <iostream>
using namespace std;

int minBags(int N){
    int qt5_max;
    qt5_max = N/5;
    if(N%5 == 0) return qt5_max;
    else{
        for(int i=qt5_max; i>=0; --i){
            if ( (N - i*5) % 3 == 0)
                return i + (N-i*5)/3;
        }
    }
    return -1;
}

int main(){
    int N;
    cin >> N;
    cout << minBags(N) << endl;
    return 0;
}
