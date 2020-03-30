#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>

#define True 0
#define False 1
using namespace std;

int main() {
    int M, N, mul, i=2;
    int* is_prime;
    vector<int> primes;

    cin >> M >> N;
    is_prime = (int*) malloc(sizeof(int) * (N-1)); // from 2 to N
    memset((void*) is_prime, 0, sizeof(is_prime));
    while(1) {
        while(is_prime[i-2] == False) {
            i++;
        }
        if(i > N) break;
        if(i >= M)
            primes.push_back(i);
        mul = 2;
        while(i * mul <= N) {
            is_prime[i*mul-2] = False;
            mul++;
        }
        i++;
    }

    for (auto i = primes.begin(); i != primes.end(); ++i)
        cout << *i << "\n";

    free(is_prime);
    return 0;
}
