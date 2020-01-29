#include <cstdio>

int D[1000001];
int N;

int main() {
    scanf("%d", &N);
    D[1] = 0;
    for(int i=2; i<=N; i++) {
        D[i] = D[i-1] + 1;
        if(i % 3 == 0 && (D[i] > D[i/3] + 1)) {
            D[i] = D[i/3] + 1;
        }
        else if(i % 2 == 0 && (D[i] > D[i/2] + 1)) {
            D[i] = D[i/2] + 1;
        }
    }
    printf("%d\n", D[N]);
}
